$(function(){
//키워드 워드클라우드 - 전체사용자
	 var data_list = $('#data_list').text()
	 //console.log(data_list)
	 var dataarray = data_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var jsonData = dataarray.replace(/'/g, '"');
	 var data = jsonData.replace(/^"|"$/g, "");
	 var validJsonString = data.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	 //console.log(validJsonString)
	
	 var resultObject = JSON.parse(validJsonString);
	 //console.log((resultObject));
	 
	 var wordCloudData = [];
	 
	 //형식에 맞게 출력
	 for (var i = 0; i < resultObject.length; i++) {
            wordCloudData.push({
                "x": resultObject[i].x,
                "value": resultObject[i].weight
            });
        }
        
	 //console.log(wordCloudData)
	 // WordCloud를 생성하고 데이터를 설정
	 var chart = anychart.tagCloud(wordCloudData);
	 //console.log(resultObject);
	  // WordCloud가 그려질 컨테이너를 지정
	 chart.container("container");
	  // 차트를 그림
	 chart.draw();
	 
	 //키워드 워드클라우드 - 회원
	 var memdata_list = $('#memdata_list').text()
	 var memdataarray = memdata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var memjsonData = memdataarray.replace(/'/g, '"');
	 var memdata = memjsonData.replace(/^"|"$/g, "");
	 var memvalidJsonString = memdata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var memresultObject = JSON.parse(memvalidJsonString);
	 
	 var memwordCloudData = [];
	 
	 //형식에 맞게 출력
	 for (var i = 0; i < memresultObject.length; i++) {
            memwordCloudData.push({
                "x": memresultObject[i].x,
                "value": memresultObject[i].weight
            });
        }
        
	 // WordCloud를 생성하고 데이터를 설정
	 var chart = anychart.tagCloud(memwordCloudData);

	 // WordCloud가 그려질 컨테이너를 지정
	 chart.container("container_mem");
	 // 차트를 그림
	 chart.draw();

	 //키워드 워드클라우드 - 비회원
	 var nmemdata_list = $('#nmemdata_list').text()
	 var nmemdataarray = nmemdata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var nmemjsonData = nmemdataarray.replace(/'/g, '"');
	 var nmemdata = nmemjsonData.replace(/^"|"$/g, "");
	 var nmemvalidJsonString = nmemdata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var nmemresultObject = JSON.parse(nmemvalidJsonString);
	 
	 var nmemwordCloudData = [];
	 
	 //형식에 맞게 출력
	 for (var i = 0; i < nmemresultObject.length; i++) {
            nmemwordCloudData.push({
                "x": nmemresultObject[i].x,
                "value": nmemresultObject[i].weight
            });
        }
        
	 // WordCloud를 생성하고 데이터를 설정
	 var chart = anychart.tagCloud(nmemwordCloudData);

	 // WordCloud가 그려질 컨테이너를 지정
	 chart.container("container_nmem");
	 // 차트를 그림
	 chart.draw();

	 //키워드 워드클라우드 - 남성10대
	 var manteen_list = $('#manteen_list').text()
	 var mteendataarray = manteen_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var mteenjsonData = mteendataarray.replace(/'/g, '"');
	 var mteendata = mteenjsonData.replace(/^"|"$/g, "");
	 var mteenvalidJsonString = mteendata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var mteenresultObject = JSON.parse(mteenvalidJsonString);
	 
	 var mteenwordCloudData = [];
	 
	 for (var i = 0; i < mteenresultObject.length; i++) {
            mteenwordCloudData.push({
                "x": mteenresultObject[i].x,
                "value": mteenresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(mteenwordCloudData);
	 chart.container("container_manteen");
	 chart.draw();
	 
	 //키워드 워드클라우드 - 남성20대
	 var mtwedata_list = $('#mantwe_list').text()
	 var mtwedataarray = mtwedata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var mtwejsonData = mtwedataarray.replace(/'/g, '"');
	 var mtwedata = mtwejsonData.replace(/^"|"$/g, "");
	 var mtwevalidJsonString = mtwedata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var mtweresultObject = JSON.parse(mtwevalidJsonString);
	 
	 var mtwewordCloudData = [];
	 
	 for (var i = 0; i < mtweresultObject.length; i++) {
            mtwewordCloudData.push({
                "x": mtweresultObject[i].x,
                "value": mtweresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(mtwewordCloudData);
	 chart.container("container_mantwe");
	 chart.draw();
	 
	 //키워드 워드클라우드 - 남성30대
	 var mthrdata_list = $('#manthr_list').text()
	 var mthrdataarray = mthrdata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var mthrjsonData = mthrdataarray.replace(/'/g, '"');
	 var mthrdata = mthrjsonData.replace(/^"|"$/g, "");
	 var mthrvalidJsonString = mthrdata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	 var mthrresultObject = JSON.parse(mthrvalidJsonString);
	 var mthrwordCloudData = [];
	 
	 for (var i = 0; i < mthrresultObject.length; i++) {
            mthrwordCloudData.push({
                "x": mthrresultObject[i].x,
                "value": mthrresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(mthrwordCloudData);
	 chart.container("container_manthr");
	 chart.draw();
	 
	 //키워드 워드클라우드 - 남성40대
	 var mfoudata_list = $('#manfou_list').text()
	 var mfoudataarray = mfoudata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var mfoujsonData = mfoudataarray.replace(/'/g, '"');
	 var mfoudata = mfoujsonData.replace(/^"|"$/g, "");
	 var mfouvalidJsonString = mfoudata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var mfouresultObject = JSON.parse(mfouvalidJsonString);
	 
	 var mfouwordCloudData = [];
	 
	 for (var i = 0; i < mfouresultObject.length; i++) {
            mfouwordCloudData.push({
                "x": mfouresultObject[i].x,
                "value": mfouresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(mfouwordCloudData);
	 chart.container("container_manfou");
	 chart.draw();
	 
	 //키워드 워드클라우드 - 남성50대
	 var mfivdata_list = $('#manfiv_list').text()
	 var mfivdataarray = mfivdata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var mfivjsonData = mfivdataarray.replace(/'/g, '"');
	 var mfivdata = mfivjsonData.replace(/^"|"$/g, "");
	 var mfivvalidJsonString = mfivdata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var mfivresultObject = JSON.parse(mfivvalidJsonString);
	 var mfivwordCloudData = [];
	 
	 for (var i = 0; i < mfivresultObject.length; i++) {
            mfivwordCloudData.push({
                "x": mfivresultObject[i].x,
                "value": mfivresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(mfivwordCloudData);
	 chart.container("container_manfiv");
	 chart.draw();
	 
	 //키워드 워드클라우드 - 남성60대이상
	 var morddata_list = $('#manord_list').text()
	 var morddataarray = morddata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var mordjsonData = morddataarray.replace(/'/g, '"');
	 var morddata = mordjsonData.replace(/^"|"$/g, "");
	 var mordvalidJsonString = morddata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var mordresultObject = JSON.parse(mordvalidJsonString);
	 
	 var mordwordCloudData = [];

	 for (var i = 0; i < mordresultObject.length; i++) {
            mordwordCloudData.push({
                "x": mordresultObject[i].x,
                "value": mordresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(mordwordCloudData);
	 chart.container("container_manord");
	 chart.draw();	 	 	 	 	 	 
	 
	 //키워드 워드클라우드 - 여성10대
	 var womanteen_list = $('#womanteen_list').text()
	 var womteendataarray = womanteen_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var womteenjsonData = womteendataarray.replace(/'/g, '"');
	 var womteendata = womteenjsonData.replace(/^"|"$/g, "");
	 var womteenvalidJsonString = womteendata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var womteenresultObject = JSON.parse(womteenvalidJsonString);
	 
	 var womteenwordCloudData = [];
	 
	 for (var i = 0; i < womteenresultObject.length; i++) {
            womteenwordCloudData.push({
                "x": womteenresultObject[i].x,
                "value": womteenresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(womteenwordCloudData);
	 chart.container("container_womanteen");
	 chart.draw();
	 
	 //키워드 워드클라우드 - 여성20대
	 var womtwedata_list = $('#womantwe_list').text()
	 var womtwedataarray = womtwedata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var womtwejsonData = womtwedataarray.replace(/'/g, '"');
	 var womtwedata = womtwejsonData.replace(/^"|"$/g, "");
	 var womtwevalidJsonString = womtwedata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var womtweresultObject = JSON.parse(womtwevalidJsonString);
	 
	 var womtwewordCloudData = [];
	 
	 for (var i = 0; i < womtweresultObject.length; i++) {
            womtwewordCloudData.push({
                "x": womtweresultObject[i].x,
                "value": womtweresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(womtwewordCloudData);
	 chart.container("container_womantwe");
	 chart.draw();
	 
	 //키워드 워드클라우드 - 여성30대
	 var womthrdata_list = $('#womanthr_list').text()
	 var womthrdataarray = womthrdata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var womthrjsonData = womthrdataarray.replace(/'/g, '"');
	 var womthrdata = womthrjsonData.replace(/^"|"$/g, "");
	 var womthrvalidJsonString = womthrdata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var womthrresultObject = JSON.parse(womthrvalidJsonString);
	 
	 var womthrwordCloudData = [];
	 
	 for (var i = 0; i < womthrresultObject.length; i++) {
            womthrwordCloudData.push({
                "x": womthrresultObject[i].x,
                "value": womthrresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(womthrwordCloudData);
	 chart.container("container_womanthr");
	 chart.draw();
	 
	 //키워드 워드클라우드 - 여성40대
	 var womfoudata_list = $('#womanfou_list').text()
	 var womfoudataarray = womfoudata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var womfoujsonData = womfoudataarray.replace(/'/g, '"');
	 var womfoudata = womfoujsonData.replace(/^"|"$/g, "");
	 var womfouvalidJsonString = womfoudata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var womfouresultObject = JSON.parse(womfouvalidJsonString);
	 
	 var womfouwordCloudData = [];
	 
	 for (var i = 0; i < womfouresultObject.length; i++) {
            womfouwordCloudData.push({
                "x": womfouresultObject[i].x,
                "value": womfouresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(womfouwordCloudData);
	 chart.container("container_womanfou");
	 chart.draw();
	 
	 //키워드 워드클라우드 - 여성50대
	 var womfivdata_list = $('#womanfiv_list').text()
	 var womfivdataarray = womfivdata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var womfivjsonData = womfivdataarray.replace(/'/g, '"');
	 var womfivdata = womfivjsonData.replace(/^"|"$/g, "");
	 var womfivvalidJsonString = womfivdata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var womfivresultObject = JSON.parse(womfivvalidJsonString);
	 var womfivwordCloudData = [];
	 
	 for (var i = 0; i < womfivresultObject.length; i++) {
            womfivwordCloudData.push({
                "x": womfivresultObject[i].x,
                "value": womfivresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(womfivwordCloudData);
	 chart.container("container_womanfiv");
	 chart.draw();
	 
	 //키워드 워드클라우드 - 여성60대이상
	 var womorddata_list = $('#womanord_list').text()
	 var womorddataarray = womorddata_list.replace("[","'[").replaceAll("'x'","x").replaceAll("'value'","value").replace("]","]'")
	 
	 var womordjsonData = womorddataarray.replace(/'/g, '"');
	 var womorddata = womordjsonData.replace(/^"|"$/g, "");
	 var womordvalidJsonString = womorddata.replace(/([{,])(\s*)([a-zA-Z0-9_]+?)\s*:/g, '$1"$3":');
	
	 var womordresultObject = JSON.parse(womordvalidJsonString);
	 
	 var womordwordCloudData = [];

	 for (var i = 0; i < womordresultObject.length; i++) {
            womordwordCloudData.push({
                "x": womordresultObject[i].x,
                "value": womordresultObject[i].weight
            });
        }
        
	 var chart = anychart.tagCloud(womordwordCloudData);
	 chart.container("container_womanord");
	 chart.draw();	
	
})