      //this graph is loaded on page load
      google.charts.load('current', {'packages':['bar']});
      google.charts.setOnLoadCallback(drawSum); 


      //##################################################################
      //<!-- if the radio buttons are selected then these graphs change -->
      //##################################################################
      
      function radioSumFunction(){
        google.charts.setOnLoadCallback(drawSum);
      };

      function radioAvgFunction(){
        google.charts.setOnLoadCallback(drawAvg);
      };


      //##################################################################
      //<!-- Sum Bar Chart-->
      //##################################################################

      function drawSum() {
        var data = google.visualization.arrayToDataTable([
          ['', 'BN', 'DEF','K','QB','R/W/T','RB','TE','WR'],
          ['Nick',185.62,74.0,62.0,162.68,39.6,141.4,36.3,121.5],
          ['Trevor',132.8,58.0,78.0,155.48,63.4,194.1,47.6,170.0],
          ['Brian',159.38,78.0,63.0,137.2,135.1,227.2,29.1,131.9],
          ['Dan',260.4,50.0,54.0,143.88,69.1,142.9,71.9,173.98],
          ['Rebecca',171.6,40.0,53.0,128.26,49.1,120.0,44.2,129.9],
          ['Tyler',282.48,72.0,52.0,187.52,65.3,195.2,51.0,125.1],
          ['Dustin',201.32,63.0,55.0,101.52,49.1,152.1,55.4,161.92],
          ['Johnny',242.54,74.0,62.0,116.66,52.6,206.6,73.8,132.1],
          ['The Robertson',231.58,32.0,66.0,127.08,75.5,81.5,29.6,192.4],
          ['Tony',275.02,51.0,35.0,135.14,61.8,179.6,31.9,204.6],
          ['Alex',226.58,31.0,68.0,170.06,48.2,113.6,74.3,129.6],
          ['Ryan',162.2,68.0,52.0,138.7,69.1,210.0,14.0,106.3]

        ]);

        var optionsSum = {
          chart: {
            title: 'Total Points by Position',
            subtitle: '2018 Season'
          },
          hAxis: {
            textStyle: {
              fontSize: 11
            },
            slantedText:true,
            slantedTextAngle:-45,
          
          },
          bars: 'vertical',
          vAxis: {format: 'decimal'},
          height: 550,
          
          chartArea:{top:100,width:'50%',height:'75%'},
          bar: { groupWidth: "75%" },
          legend: { position: 'top', alignment: 'center' }
        };

        var chart = new google.charts.Bar(document.getElementById('barChart'));

        chart.draw(data, google.charts.Bar.convertOptions(optionsSum));      
      }



      //##################################################################
      //<!-- Average Bar Chart -->
      //##################################################################


      function drawAvg() {
        var data = google.visualization.arrayToDataTable([
          ['', 'BN', 'DEF','K','QB','R/W/T','RB','TE','WR'],
          ['Nick',26.52,10.57,8.86,23.24,5.66,20.2,5.19,17.36],
          ['Trevor',18.97,8.29,11.14,22.21,9.06,27.73,6.8,24.29],
          ['Brian',22.77,11.14,9.0,19.6,19.3,32.46,4.16,18.84],
          ['Dan',37.2,7.14,7.71,20.55,9.87,20.41,10.27,24.85],
          ['Rebecca',24.51,5.71,7.57,18.32,7.01,17.14,6.31,18.56],
          ['Tyler',40.35,10.29,7.43,26.79,9.33,27.89,7.29,17.87],
          ['Dustin',28.76,9.0,7.86,14.5,7.01,21.73,7.91,23.13],
          ['Johnny',34.65,10.57,8.86,16.67,7.51,29.51,10.54,18.87],
          ['The Robertson',33.08,4.57,9.43,18.15,10.79,11.64,4.23,27.49],
          ['Tony',39.29,7.29,5.0,19.31,8.83,25.66,4.56,29.23],
          ['Alex',32.37,4.43,9.71,24.29,6.89,16.23,10.61,18.51],
          ['Ryan',23.17,9.71,7.43,19.81,9.87,30.0,2.0,15.19]

        ]);

        var optionsAvg = {
          chart: {
            title: 'Average Points by Position',
            subtitle: '2018 Season'
          },
          hAxis: {
            titleTextStyle: {
              color: '#FF0000',            
            },
            textStyle: {
              fontSize: 11
            },
            slantedText:true,
            slantedTextAngle:-45,
          
          },
          bars: 'vertical',
          vAxis: {format: 'decimal'},
          height: 550,
          chartArea:{top:100,width:'50%',height:'75%'},
          bar: { groupWidth: "75%" },
          legend: { position: 'top', alignment: 'center' }
        };

        var chart = new google.charts.Bar(document.getElementById('barChart'));

        chart.draw(data, google.charts.Bar.convertOptions(optionsAvg));      
      }



      //##################################################################
      //<!-- Scatter Plot -->
      //##################################################################

      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['For','Alex','Brian','Dan','Dustin','Johnny','Nick','Rebecca','Ryan','The Robertson','Tony','Trevor','Tyler'],
          [564.46,NaN,NaN,NaN,NaN,NaN,NaN,737.68,NaN,NaN,NaN,NaN,NaN],
          [604.18,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,677.8,NaN,NaN,NaN],
          [634.8,635.64,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN],
          [637.48,NaN,NaN,NaN,NaN,NaN,667.3,NaN,NaN,NaN,NaN,NaN,NaN],
          [638.04,NaN,NaN,NaN,711.3,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN],
          [658.0,NaN,NaN,NaN,NaN,NaN,NaN,NaN,679.36,NaN,NaN,NaN,NaN],
          [699.04,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,677.82,NaN,NaN],
          [705.76,NaN,NaN,728.98,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN],
          [717.76,NaN,NaN,NaN,NaN,646.9,NaN,NaN,NaN,NaN,NaN,NaN,NaN],
          [748.12,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,684.38],
          [766.58,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,663.76,NaN],
          [801.3,NaN,664.6,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN]




        ]);

        var scatterOptions = {
          title: 'Points For vs Points Against',
          hAxis: {title: 'Points For'},
          vAxis: {title: 'Points Against'},
          legend: 'none',
          height: 750,
          chartArea:{top:100,width:'50%',height:'75%'}
        };

        var chart = new google.visualization.ScatterChart(document.getElementById('scatterChart'));

        chart.draw(data, scatterOptions);
      }


      //##################################################################
      //<!-- Table  -->
      //##################################################################


      google.charts.load('current', {'packages':['table']});
      google.charts.setOnLoadCallback(drawTable);

      function drawTable() {
        var data = google.visualization.arrayToDataTable([
	      ['Team Owner', 'Power Ranking'],
	      ['Trevor',1.0],
		  ['Brian',2.0],
		  ['Tyler',3.0],
		  ['Dan',4.0],
		  ['Johnny',5.0],
		  ['Tony',6.0],
		  ['Dustin',7.0],
		  ['Alex',8.0],
		  ['Ryan',9.0],
		  ['The Robertson',10.0],
		  ['Nick',11.0],
		  ['Rebecca',12.0]

        ]);


        var tableOptions = {
          title: 'Points For vs Points Against',
          showRowNumber: true,
          width: '40%',
          height: '40%'
        };

        var table = new google.visualization.Table(document.getElementById('table_div'));

        table.draw(data, tableOptions);
      }      


