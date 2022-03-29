const Test = 1

class Helpers {
    static RandomColor() {
        return Math.floor(Math.random() * 16777215).toString(16);
    }
}

class Charts {
    static CreateBarChartStyle(items) {
        var colors = []
        for (let i = 0; i < items; i++) {
            colors.push("#2b2b2b")
        }
        return {
            backgroundColor: colors
        }
    }

    static CreateLoadingElement(id) {
        return "<div id='loading_" + id + "' class=\"text-center\">\n" +
            "    <span>Loading ...</span><br>\n" +
            "  <div class=\"spinner-border text-primary\" role=\"status\">\n" +
            "    <span class=\"visually-hidden\">Loading...</span>\n" +
            "  </div>\n" +
            "</div>"
    }

    static CreateErrorPane(msg) {
        return "<div class=\"text-center\">\n" +
            "<i class=\"fas fa-times fa-2x\" style='color: #d9534f'><br>ERROR</i><br>\n" +
            "<span>" + msg + "<span><br>\n" +
            "</div>"
    }

    static CreateLineStyle() {
        return {
            fill: false,
            borderColor: "#FFFDDD",
            tension: 0.3
        }
    }

    static CreateLineChartLocal(cid, data) {
        const ctx = document.getElementById(cid).getContext('2d');
        for (let i = data['datasets'].length - 1; i >= 0; i--) {
            $.extend(data['datasets'][i], Charts.CreateLineStyle());
        }
        new Chart(ctx, {
            options: {
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        title: {
                            color: "#FFFFFF",
                        },
                        labels: {
                            color: "white",
                            fontSize: 18
                        }
                    }
                },
                scales: {
                    x: {  // <-- axis is not array anymore, unlike before in v2.x: '[{'
                        grid: {
                            color: '#FFFFFF',
                        }
                    },
                    y: {  // <-- axis is not array anymore, unlike before in v2.x: '[{'
                        grid: {
                            color: '#FFFFFF',
                        }
                    }
                }
            },
            type: 'line',
            data: data
        });

    }

    static CreateLineChart(cid, data_url) {
        const container = document.getElementById(cid).parentElement
        container.innerHTML = this.CreateLoadingElement()
        console.log(data_url)
        $.ajax({
            type: 'GET',
            headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value},
            url: data_url,
            success: function (response) {
                const canvas = document.createElement('canvas');
                canvas.id = cid
                container.innerHTML = canvas.outerHTML
                const ctx = document.getElementById(cid).getContext('2d');

                for (let i = response['datasets'].length - 1; i >= 0; i--) {
                    $.extend(response['datasets'][i], Charts.CreateLineStyle());
                }
                new Chart(ctx, {
                    options: {
                        maintainAspectRatio: false,
                    },
                    type: 'line',
                    data: response
                });
            },
            error: function (response) {
                container.innerHTML = Charts.CreateErrorPane(response.responseText)
            },
        });
    }

    static CreateSleepCharLocal(cid, data) {
        const ctx = document.getElementById(cid).getContext('2d');
        const myChart = new Chart(ctx, {
            options: {
                maintainAspectRatio: false,
                scales: {
                    hours: {
                        type: 'linear',
                        display: true,
                        position: 'left',
                        beginAtZero: true,
                        ticks: {
                            color: "#FFFFFF"
                        },
                        grid: {
                            color: "#FFFFFF"
                        },
                        title: {
                            color: "#FFFFFFs"
                        }
                    },
                    interruptions: {
                        type: 'linear',
                        display: true,
                        position: 'right',
                        beginAtZero: true,
                        ticks: {
                            color: "#FFFFFF"
                        }
                    },
                }
            },
            data: data
        });
    }

    static CreateSleepChart(cid, data_url) {
        const container = document.getElementById(cid).parentElement
        container.innerHTML = this.CreateLoadingElement()
        console.log(data_url)
        $.ajax({
            type: 'GET',
            headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value},
            url: data_url,
            success: function (response) {
                const canvas = document.createElement('canvas');
                canvas.id = cid
                container.innerHTML = canvas.outerHTML
                const ctx = document.getElementById(cid).getContext('2d');
                const myChart = new Chart(ctx, {
                    options: {
                        maintainAspectRatio: false,
                        scales: {
                            hours: {
                                type: 'linear',
                                display: true,
                                position: 'left',
                                beginAtZero: true
                            },
                            interruptions: {
                                type: 'linear',
                                display: true,
                                position: 'right',
                                beginAtZero: true
                            },
                        }
                    },
                    data: response
                });
            },
            error: function (response) {
                container.innerHTML = Charts.CreateErrorPane(response.responseText)
            },
        });
    }
}
