const ROOT_URL = 'http://localhost:5000'
//const ROOT_URL = 'https://hermann-nfl-offense-dashboard.herokuapp.com'

function makeLayout(xAxis, yAxis) {

    // update headers
    document.getElementById("plot-title").innerText = xAxis + ' And ' + yAxis;
    document.getElementById("table-title").innerText = xAxis + ' And ' + yAxis;

    var layout = {
        margin: {
            l: 60,
            r: 0,
            b: 50,
            t: 0
        },
        xaxis: {
            title: {
                text: xAxis,
                    font: {
                        family: 'Sans Serif',
                        size: 24,
                            color: '#7f7f7f'
                }
            },
        },
        yaxis: {
            title: {
                text: yAxis,
                    font: {
                        family: 'Sans Serif',
                        size: 24,
                            color: '#7f7f7f'
                }
            }
        }
    }

    return layout
}

function createTable(d, x, y) {

    // update table data
    var tableData = []
    for (var ind = 0; ind < Object.values(d.name).length; ind++) {
        tableData.push({
            'name': Object.values(d.name)[ind],
            'x': Object.values(d[toSnakeCase(x)])[ind],
            'y': Object.values(d[toSnakeCase(y)])[ind]
        })
    }

    // load table data
    $(function () {
        if ($.fn.dataTable.isDataTable('#data-table')) {
            table = $('#data-table').DataTable({ 
                retrieve: true 
            });
            table.destroy()
        }

        // create or recreate data table - documentation @ datatables.net
        $('#data-table').DataTable({
            data: tableData,
            columns: [
                { data: 'name'},
                { data: 'x'},
                { data: 'y'}
            ],
            searching: false,
            pagingType: "full",
            columnDefs: [{ "title": "Name", "targets": 0 }, { "title": toTitleCase(x), "targets": 1 }, { "title": toTitleCase(y), "targets": 2 }],
            responsive: true
        })

        $('#data-table').bootstrapTable("hideLoading")

    })

    // bootstrap updates too quickly to change headers without timeout....
    setTimeout(updateTableHeaders, 1000)

    function updateTableHeaders(){
        if ($('.th-inner').text().length > 0){
            
            var arr = [x, y]

            // update headers of x and y
            $('.th-inner').each(function (index, obj){
                if(index > 0){
                    $(this).html(toTitleCase(arr[index-1]))
                }
            })
        }

        
    }

}

function createScatter(table, x, y) {
    d3.json(`${ROOT_URL}/${toSnakeCase(table)}/${toSnakeCase(x)}/${toSnakeCase(y)}`).then((d) =>{

        // check for incorrect input
        if(d.length === 0){
            alert('Please choose different x and y values!')
            return
        }

        // update table
        createTable(d, x, y)

        // create scatter plot
        var layout = makeLayout(toTitleCase(x), toTitleCase(y))
        var plot = document.getElementById('plot');

        // setup trace
        var trace = {
            x: Object.values(d[toSnakeCase(x)]),
            y: Object.values(d[toSnakeCase(y)]),
            text: Object.values(d.name),
            mode: 'markers',
            type: 'scatter'
        }

        // setup data
        var data = [trace]

        // create plot
        Plotly.newPlot(plot, data, layout, { responsive: true, displayModeBar: false })
    })
}

function updateScatter() {

    // get table selection
    var selector = document.getElementById('table-selector-dropdown')
    var table = selector.options[selector.selectedIndex].value.toLowerCase()

    // get x choice
    var xAxis = document.getElementById('x-selector-dropdown')
    var xAxis = xAxis.options[xAxis.selectedIndex].value.toLowerCase()

    // get y choice
    var yAxis = document.getElementById('y-selector-dropdown')
    var yAxis = yAxis.options[yAxis.selectedIndex].value.toLowerCase()

    //create scatter plot
    createScatter(table, xAxis, yAxis)
}

function updateSelectors() {

    var selector = document.getElementById('table-selector-dropdown')
    var table = selector.options[selector.selectedIndex].value.toLowerCase()

    // axies dropdowns
    var x = document.getElementById('x-selector-dropdown')
    var y = document.getElementById('y-selector-dropdown')

    var options = ''
    d3.json(`${ROOT_URL}/${toSnakeCase(table)}`).then((d) => {
        
        // create options
        for (var selection of d) {
            options += "<option>" + toTitleCase(selection) + "</option>"
        }

        // add options
        x.innerHTML = options
        y.innerHTML = options
    })

}

function toTitleCase(str) {
    
    // split string into words
    var words = str.split('_')
    var outputWords = ''

    // concatenate words together with space
    for(var word of words){
        outputWords += word + ' '
    }

    // convert to proper casing
    var output = outputWords.charAt(0).toUpperCase() + outputWords.substr(1).toLowerCase()

    return output.trim();
}

function toSnakeCase(str) {

    // split string into words
    var words = str.split(' ')
    var outputWords = ''

    // concatenate words together with space
    if(words.length > 1){
        for (var word of words) {
            outputWords += word + '_'
        }
        outputWords = outputWords.substr(0, outputWords.length - 1)
    } else {
        outputWords = str
    }

    // convert to proper casing
    var output = outputWords.toLowerCase().trim()

    return output;

}


$(document).ready(() => {

    // default graph
    createScatter('passing', 'passing_yards', 'passing_tds')
    
    // create event listener
    d3.selectAll('#submitBtn').on('click', updateScatter)
    d3.selectAll('#table-selector-dropdown').on('change', updateSelectors)
})

