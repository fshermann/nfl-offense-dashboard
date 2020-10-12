var passing_layout = {
    title: {
        text: 'NFL Passing Yards Vs Passing Touchdowns',
        font: {
            family: 'Helvetica Neue',
            size: 36
        },
        xref: 'paper',
        x: 0.05,
    },
    xaxis: {
        title: {
            text: 'Passing Yards',
            font: {
                family: 'Helvetica Neue',
                size: 24,
                color: '#7f7f7f'
            }
        },
    },
    yaxis: {
        title: {
            text: 'Passing Touchdowns',
            font: {
                family: 'Helvetica Neue',
                size: 24,
                color: '#7f7f7f'
            }
        }
    }
}

var rushing_layout = {
    title: {
        text: 'NFL Rushing Yards Vs Rushing Touchdowns',
        font: {
            family: 'Helvetica Neue',
            size: 36
        },
        xref: 'paper',
        x: 0.05,
    },
    xaxis: {
        title: {
            text: 'Rushing Yards',
            font: {
                family: 'Helvetica Neue',
                size: 24,
                color: '#7f7f7f'
            }
        },
    },
    yaxis: {
        title: {
            text: 'Rushing Touchdowns',
            font: {
                family: 'Helvetica Neue',
                size: 24,
                color: '#7f7f7f'
            }
        }
    }
}
d3.json('https://hermann-nfl-offense-dashboard.herokuapp.com/passing-yards-tds').then((d) =>{
    // create scatter plot
    var passing_plot = document.getElementById('plot');
    var trace = {
        x: Object.values(d.passing_yards),
        y: Object.values(d.passing_tds),
        text: Object.values(d.name),
        mode: 'markers',
        type: 'scatter'
    }
    var data = [trace]
    Plotly.newPlot(passing_plot, data, passing_layout)
})

d3.json('https://hermann-nfl-offense-dashboard.herokuapp.com/rushing-yards-tds').then((d) => {
    // create scatter plot
    var rushing_plot = document.getElementById('plot2');
    var trace = {
        x: Object.values(d.rushing_yards),
        y: Object.values(d.rushing_tds),
        text: Object.values(d.name),
        mode: 'markers',
        type: 'scatter'
    }
    var data = [trace]
    Plotly.newPlot(rushing_plot, data, rushing_layout)
})

