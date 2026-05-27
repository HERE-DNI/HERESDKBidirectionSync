---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-roadshieldiconproperties-routenumbername"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- routeNumberName.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/RoadShieldIconProperties-class.html">/sdk-for-flutter-explore-mapview-roadshieldiconproperties-class</a></li>
<li class="self-crumb">routeNumberName property</li>
</ol>
<div class="self-name">routeNumberName</div>
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
<div class="main-content" data-above-sidebar="mapview/RoadShieldIconProperties-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>routeNumberName property</h1></div>
<section class="multi-line-signature">
        
        String
        routeNumberName
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>A string that is used to additionally determine the road shield's visual representation.
In a routing context, the text can be taken from a <code>LocalizedRoadNumber</code>, which
is available for each <code>Span</code> of a <code>Route</code> object.
Typically, the string contains the number of a road, such as "E100". Internally, the text
is parsed with a RegEx pattern and the results will be used along with other properties
such as <code>routeType</code>, <code>countryCode</code> and <code>stateCode</code> to identify the visual representation
of a road shield icon.</p>
<p>Note that the actual text which will be displayed on the road shield icon is set with
<a href="../../mapview/RoadShieldIconProperties/shieldText.html">/sdk-for-flutter-explore-mapview-roadshieldiconproperties-shieldtext</a>. In order to determine the visuals of the icon, <code>countryCode</code>, <code>routeType</code>
and eventually the <code>stateCode</code> is in most cases sufficient to determine the type of road
shield. In this case an empty string should be passed.</p>
<p><strong>Note:</strong> Texts that contain a <code>CardinalDirection</code> are currently not supported and may lead
to unexpected results. See <code>LocalizedRoadNumber</code> for more details, it provides texts with
and without a cardinal direction.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String routeNumberName;</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/RoadShieldIconProperties-class.html">/sdk-for-flutter-explore-mapview-roadshieldiconproperties-class</a></li>
<li class="self-crumb">routeNumberName property</li>
</ol>
<h5>RoadShieldIconProperties class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
</HTMLBlock>
