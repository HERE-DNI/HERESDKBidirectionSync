---
title: "OfflineSearchEngine class abstract"
slug: "sdk-for-flutter-navigate-search-offlinesearchengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- OfflineSearchEngine-class.html -->


<div>
<h1>OfflineSearchEngine class abstract</h1></div>

<p>The OfflineSearchEngine works without internet and unlocks the search and geocoding
capabilities of HERE services to provide developers with unmatched flexibility
to create differentiating location-enabled applications.</p>
<p>It provides the same interfaces as the SearchEngine, but the results may slightly
differ as the results are taken from already downloaded map data instead of initiating
a new request to a HERE backend service. This way the data may be, for example, older
compared to the data you may receive when using the SearchEngine. On the other hand,
this class provides results faster as no online connection is necessary.</p>
<p>In comparison to the SearchEngine, there are a few limitations:</p>
<ul>
<li>The IDs of POIs are different and may differ among different map versions.</li>
<li>The implementation is different and the resources are limited, so the results can differ.</li>
<li>OfflineSearchEngine sometimes doesn't return the requested number of results.</li>
</ul>
<p>Note: You can search only within persistent map data (downloaded via MapDownloader) or existing cached data.
However, cached data may be incomplete, which can result in searches returning partial or incomplete information.
Therefore, it is recommended to use persistent map data.
Make sure that at least <a href="/sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.offlineSearch</a> is enabled.
For EV rich attributes also enable <a href="/sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.ev</a>,
for truck rich attributes also enable <a href="/sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.truckServiceAttributes</a>,
for fuel station rich attributes also enable <a href="/sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.fuelStationAttributes</a>
in <a href="/sdk-for-flutter-navigate-core-engine-sdkoptions-layerconfiguration">SDKOptions.layerConfiguration</a>.</p>


<ul><li>Implemented types</li></ul>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-navigate-search-offlinesearchengine-offlinesearchengine">OfflineSearchEngine</a></li><li><a href="/sdk-for-flutter-navigate-search-offlinesearchengine-offlinesearchengine-withsdkengine">OfflineSearchEngine.withSdkEngine</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-navigate-search-searchinterface-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-navigate-search-searchinterface-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-navigate-search-offlinesearchengine-attach">attach</a></li><li><a href="/sdk-for-flutter-navigate-search-searchinterface-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-navigate-search-searchinterface-searchbyaddress">searchByAddress</a></li><li><a href="/sdk-for-flutter-navigate-search-offlinesearchengine-searchbyaddresselements">searchByAddressElements</a></li><li><a href="/sdk-for-flutter-navigate-search-searchinterface-searchbycategory">searchByCategory</a></li><li><a href="/sdk-for-flutter-navigate-search-searchinterface-searchbycoordinates">searchByCoordinates</a></li><li><a href="/sdk-for-flutter-navigate-search-searchinterface-searchbypickedplace">searchByPickedPlace</a></li><li><a href="/sdk-for-flutter-navigate-search-searchinterface-searchbyplaceid">searchByPlaceId</a></li><li><a href="/sdk-for-flutter-navigate-search-searchinterface-searchbytext">searchByText</a></li><li><a href="/sdk-for-flutter-navigate-search-offlinesearchengine-suggestbyaddresselements">suggestByAddressElements</a></li><li><a href="/sdk-for-flutter-navigate-search-searchinterface-suggestbytext">suggestByText</a></li><li><a href="/sdk-for-flutter-navigate-search-searchinterface-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-navigate-search-searchinterface-operator-equals">operator ==</a></li></ul>


<h2>Static Methods</h2>
<ul><li><a href="/sdk-for-flutter-navigate-search-offlinesearchengine-setindexoptions">setIndexOptions</a></li></ul>

 



</div>
`
}</HTMLBlock>
