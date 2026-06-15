---
title: "SearchEngine class abstract"
slug: "sdk-for-flutter-explore-search-searchengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SearchEngine-class.html -->


<div>
<h1>SearchEngine class abstract</h1></div>

<p>The SearchEngine API unlocks the search, geocoding and suggesting capabilities of HERE services
to provide developers with unmatched flexibility to create differentiating location-enabled
applications.</p>
<p>It enables to search for HERE points of interests, forward and reverse
geocode addresses and geographic coordinates from the HERE map and search for suggested addresses
or place candidates based on incomplete or misspelled queries.</p>
<p>It also allows to search along a given <a href="sdk-for-flutter-explore-core-geopolyline-class">GeoPolyline</a> set inside a <a href="sdk-for-flutter-explore-core-geocorridor-class">GeoCorridor</a>
as part of a <a href="sdk-for-flutter-explore-search-textquery-class">TextQuery</a>.</p>
<p>The SearchEngine API requires an online connection to execute the requests.</p>
<p><strong>Note:</strong> All methods are provided in two flavors. One uses a <a href="sdk-for-flutter-explore-search-searchcallback">SearchCallback</a> and the
other uses a <a href="sdk-for-flutter-explore-search-searchcallbackextended">SearchCallbackExtended</a>: The later adds a <code>ResponseDetails</code> result type
that provides the <code>requestId</code> of a search request and a <code>correlationId</code> to identify multiple,
related queries. This may be useful for debug purposes.</p>


<ul><li>Implemented types</li></ul>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-explore-search-searchengine-searchengine">SearchEngine</a></li><li><a href="sdk-for-flutter-explore-search-searchengine-searchengine-withsdkengine">SearchEngine.withSdkEngine</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-explore-search-searchinterface-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-explore-search-searchinterface-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-explore-search-searchinterface-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-explore-search-searchinterface-searchbyaddress">searchByAddress</a></li><li><a href="sdk-for-flutter-explore-search-searchengine-searchbyaddressextended">searchByAddressExtended</a></li><li><a href="sdk-for-flutter-explore-search-searchinterface-searchbycategory">searchByCategory</a></li><li><a href="sdk-for-flutter-explore-search-searchengine-searchbycategoryextended">searchByCategoryExtended</a></li><li><a href="sdk-for-flutter-explore-search-searchinterface-searchbycoordinates">searchByCoordinates</a></li><li><a href="sdk-for-flutter-explore-search-searchengine-searchbycoordinatesextended">searchByCoordinatesExtended</a></li><li><a href="sdk-for-flutter-explore-search-searchengine-searchbycoordinateswithradius">searchByCoordinatesWithRadius</a></li><li><a href="sdk-for-flutter-explore-search-searchengine-searchbycoordinateswithradiusextended">searchByCoordinatesWithRadiusExtended</a></li><li><a href="sdk-for-flutter-explore-search-searchinterface-searchbypickedplace">searchByPickedPlace</a></li><li><a href="sdk-for-flutter-explore-search-searchinterface-searchbyplaceid">searchByPlaceId</a></li><li><a href="sdk-for-flutter-explore-search-searchengine-searchbyplaceidwithlanguagecodeextended">searchByPlaceIdWithLanguageCodeExtended</a></li><li><a href="sdk-for-flutter-explore-search-searchinterface-searchbytext">searchByText</a></li><li><a href="sdk-for-flutter-explore-search-searchengine-searchbytextextended">searchByTextExtended</a></li><li><a href="sdk-for-flutter-explore-search-searchengine-sendrequest">sendRequest</a></li><li><a href="sdk-for-flutter-explore-search-searchengine-sendrequestextended">sendRequestExtended</a></li><li><a href="sdk-for-flutter-explore-search-searchengine-setcustomoption">setCustomOption</a></li><li><a href="sdk-for-flutter-explore-search-searchengine-setevinterface">setEVInterface</a></li><li><a href="sdk-for-flutter-explore-search-searchinterface-suggestbytext">suggestByText</a></li><li><a href="sdk-for-flutter-explore-search-searchengine-suggestextended">suggestExtended</a></li><li><a href="sdk-for-flutter-explore-search-searchinterface-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-explore-search-searchinterface-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
