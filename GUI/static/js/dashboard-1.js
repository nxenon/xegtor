

(function($) {
    /* "use strict" */
	
 var dzChartlist = function(){
	
	var screenWidth = $(window).width();	
	
	var radialChart = function(){
		var options = {
		  series: [70],
		  chart: {
		  height: 150,
		  type: 'radialBar',
		  sparkline:{
			  enabled:true
		  }
		},
		plotOptions: {
		  radialBar: {
			hollow: {
			  size: '35%',
			},
			dataLabels: {
              show: false,
			}
		  },
		},
		labels: [''],
		};

		var chart = new ApexCharts(document.querySelector("#radialChart"), options);
		chart.render();
	}
	
	var reservationChart = function(){
		 var options = {
          series: [{
          name: 'series1',
          data: [400, 400, 650, 500, 900, 750, 850 ,600, 950, 500, 650, 700]
        }, {
          name: 'series2',
          data: [350, 350, 420, 370, 500, 400, 550, 420, 600, 450, 550, 400]
        }],
          chart: {
          height: 400,
          type: 'area',
		  toolbar:{
			  show:false
		  }
        },
		colors:["#1362FC","#FF6E5A"],
        dataLabels: {
          enabled: false
        },
        stroke: {
			width:6,
			curve: 'smooth',
        },
		legend:{
			show:false
		},
		grid:{
			borderColor: '#EBEBEB',
			strokeDashArray: 6,
		},
		markers:{
			strokeWidth: 6,
			 hover: {
			  size: 15,
			}
		},
		yaxis: {
		  labels: {
			offsetX:-12,
			style: {
				colors: '#787878',
				fontSize: '13px',
				fontFamily: 'Poppins',
				fontWeight: 400
				
			}
		  },
		},
        xaxis: {
          categories: ["01","02","03","04","05","06","07","08","09","10","11","12"],
		  labels:{
			  style: {
				colors: '#787878',
				fontSize: '13px',
				fontFamily: 'Poppins',
				fontWeight: 400
				
			},
		  }
        },
		fill:{
			type:"solid",
			opacity:0.1
		},
        tooltip: {
          x: {
            format: 'dd/MM/yy HH:mm'
          },
        },
        };

        var chart = new ApexCharts(document.querySelector("#reservationChart"), options);
        chart.render();
	}
	
	var donutChart = function(){
		$("span.donut").peity("donut", {
			width: 150,
			height: 150
		});
		if ( $(window).width() <= 1600 ) {
			$("span.donut").peity("donut", {width: '110', height: '110'});
		} else {
			$("span.donut").peity("donut", {width: '150', height: '150'});
		}
		$(window).resize(function(){
			if ( $(window).width() <= 1600 ) {
				$("span.donut").peity("donut", {width: '110', height: '110'});
			} else {
				$("span.donut").peity("donut", {width: '150', height: '150'});
			}
		})
		
	}
	
	/* Function ============ */
		return {
			init:function(){
				
			},
			
			load:function(){
				radialChart();
				reservationChart();
				donutChart();
			},
			
			resize:function(){
			}
		}
	
	}();

	
		
	jQuery(window).on('load',function(){
		setTimeout(function(){
			dzChartlist.load();
		}, 1000); 
		
	});

     

})(jQuery);