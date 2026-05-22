---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-roadsignwarningoptions-vehicletypesfilter"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- vehicleTypesFilter.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-roadsignwarningoptions-class</li>
<li class="self-crumb">vehicleTypesFilter property</li>
</ol>
<div class="self-name">vehicleTypesFilter</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="navigation/RoadSignWarningOptions-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>vehicleTypesFilter property</h1></div>
<section class="multi-line-signature">
        
        List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-roadsignvehicletype&gt;
vehicleTypesFilter
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>The list of road sign vehicle types for which a warning will be given. If the list is empty,
road signs are not filtered by vehicle type, which means that you get road sign warnings for all vehicle types.</p>
<p><strong>Example:</strong> For a filter that contains only bus and trucks you will only receive specific road sign warnings for
bus and trucks - you will not get signs for the other types, such as heavy trucks or motorhomes.
Furthermore, you will <em>not</em> get any signs that are generally applicable for all vehicles. For example,
you cannot set a filter that allows to get signs for trucks <em>and</em> cars. If you want to get signs for standard vehicles
like cars, then the only option is to set an empty list as filter.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;RoadSignVehicleType&gt; vehicleTypesFilter;</code></pre>
</section>
</div> 
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">

<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-roadsignwarningoptions-class</li>
<li class="self-crumb">vehicleTypesFilter property</li>
</ol>
<h5>RoadSignWarningOptions class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
