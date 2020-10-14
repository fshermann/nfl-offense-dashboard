function makeLayout( xAxis, yAxis) {

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

d3.json('https://hermann-nfl-offense-dashboard.herokuapp.com/passing-yards-tds').then((d) =>{
    // create scatter plot

    var layout = makeLayout("Passing Yards", "Passing Touchdowns")
    var plot = document.getElementById('plot');
    var trace = {
        x: Object.values(d.passing_yards),
        y: Object.values(d.passing_tds),
        text: Object.values(d.name),
        mode: 'markers',
        type: 'scatter'
    }
    var data = [trace]
    Plotly.newPlot(plot, data, layout, { responsive: true, displayModeBar: false })
})