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
          ['Nick',307.92,84.0,85.0,229.82,64.7,212.3,56.9,159.0],
          ['Trevor',204.6,86.0,118.0,219.34,78.3,316.7,62.7,254.8],
          ['Brian',223.54,99.0,93.0,175.24,193.8,298.7,41.4,175.3],
          ['Dan',313.0,91.0,72.0,197.64,88.1,209.9,78.6,252.58],
          ['Rebecca',203.62,74.0,77.0,206.16,83.0,176.8,61.5,186.9],
          ['Tyler',378.44,117.0,68.0,260.4,83.4,291.1,72.9,202.92],
          ['Dustin',286.66,58.0,74.0,143.1,57.1,271.6,72.0,224.62],
          ['Johnny',325.8,79.0,81.0,168.52,88.1,265.8,125.7,152.0],
          ['The Robertson',338.24,56.0,92.0,205.3,91.9,137.0,47.2,277.8],
          ['Tony',359.1,75.0,58.0,179.58,94.2,293.1,38.3,279.5],
          ['Alex',271.18,56.0,89.0,241.2,61.4,194.5,114.7,200.4],
          ['Ryan',186.5,65.0,71.0,215.56,86.7,315.0,48.8,143.5]


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
          ['Nick',30.79,8.4,8.5,22.98,6.47,21.23,5.69,15.9],
          ['Trevor',20.46,8.6,11.8,21.93,7.83,31.67,6.27,25.48],
          ['Brian',22.35,9.9,9.3,17.52,19.38,29.87,4.14,17.53],
          ['Dan',31.3,9.1,7.2,19.76,8.81,20.99,7.86,25.26],
          ['Rebecca',20.36,7.4,7.7,20.62,8.3,17.68,6.15,18.69],
          ['Tyler',37.84,11.7,6.8,26.04,8.34,29.11,7.29,20.29],
          ['Dustin',28.67,5.8,7.4,14.31,5.71,27.16,7.2,22.46],
          ['Johnny',32.58,7.9,8.1,16.85,8.81,26.58,12.57,15.2],
          ['The Robertson',33.82,5.6,9.2,20.53,9.19,13.7,4.72,27.78],
          ['Tony',35.91,7.5,5.8,17.96,9.42,29.31,3.83,27.95],
          ['Alex',27.12,5.6,8.9,24.12,6.14,19.45,11.47,20.04],
          ['Ryan',18.65,6.5,7.1,21.56,8.67,31.5,4.88,14.35]


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
          [1017.68,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,1041.82,NaN,NaN],
          [1076.24,NaN,922.04,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN],
          [1095.72,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,972.12],
          [1135.84,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,979,NaN],
          [865.36,NaN,NaN,NaN,NaN,NaN,NaN,1045.46,NaN,NaN,NaN,NaN,NaN],
          [891.72,NaN,NaN,NaN,NaN,NaN,928.82,NaN,NaN,NaN,NaN,NaN,NaN],
          [900.42,NaN,NaN,NaN,1046.78,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN],
          [907.3,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,971.44,NaN,NaN,NaN],
          [945.46,NaN,NaN,NaN,NaN,NaN,NaN,NaN,933.78,NaN,NaN,NaN,NaN],
          [957.24,974.24,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN],
          [960.12,NaN,NaN,NaN,NaN,924.48,NaN,NaN,NaN,NaN,NaN,NaN,NaN],
          [989.82,NaN,NaN,1002.94,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN,NaN]





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
	      ['Trevor',1.0],
        ['Tyler',2.0],
        ['Tony',3.0],
        ['Alex',4.0],
        ['Brian',5.0],
        ['The Robertson',6.0],
        ['Ryan',7.0],
        ['Dan',8.0],
        ['Dustin',9.0],
        ['Rebecca',10.0],
        ['Johnny',11.0],
        ['Nick',12.0]


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


