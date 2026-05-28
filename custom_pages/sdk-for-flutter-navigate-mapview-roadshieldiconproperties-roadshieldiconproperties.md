---
title: "RoadShieldIconProperties constructor"
slug: "sdk-for-flutter-navigate-mapview-roadshieldiconproperties-roadshieldiconproperties"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoadShieldIconProperties.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-roadshieldiconproperties-class</li>
<li class="self-crumb">RoadShieldIconProperties constructor</li>
</ol>
<div class="self-name">RoadShieldIconProperties</div>
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
<h1>RoadShieldIconProperties constructor</h1></div>
<section class="multi-line-signature">
RoadShieldIconProperties(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-navigate-core-routetype routeType, </li>
<li>String countryCode, </li>
<li>String stateCode, </li>
<li>String routeNumberName, </li>
<li>String shieldText, </li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>routeType</code> The type of route indicating the significance of the road in a range from 0 to 6. A value of
1 stands for the most major route and 6 the most minor, with 0 being of unknown type.</li>
<li><code>countryCode</code> The country code in ISO-3166-1 alpha-3 format, which will determine the type of road shield.</li>
<li><code>stateCode</code> The state code for the road. It's a 2-letter code in ISO 3166-2 format. For example
the ones listed for US on this page <a href="https://en.wikipedia.org/wiki/ISO_3166-2:US">https://en.wikipedia.org/wiki/ISO_3166-2:US</a>.
The code "AL" is for Alabama. Another example is the code for autonomous
communities listed on <a href="https://en.wikipedia.org/wiki/ISO_3166-2:ES">https://en.wikipedia.org/wiki/ISO_3166-2:ES</a>. Can be empty if
not required for the particular country.</li>
<li><code>routeNumberName</code> A string that is used to additionally determine the road shield's visual representation.
In a routing context, the text can be taken from a <code>LocalizedRoadNumber</code>, which
is available for each <code>Span</code> of a <code>Route</code> object.
Typically, the string contains the number of a road, such as "E100". Internally, the text
is parsed with a RegEx pattern and the results will be used along with other properties
such as <code>routeType</code>, <code>countryCode</code> and <code>stateCode</code> to identify the visual representation
of a road shield icon.</li>
</ul>
<p>Note that the actual text which will be displayed on the road shield icon is set with
/sdk-for-flutter-navigate-mapview-roadshieldiconproperties-shieldtext. In order to determine the visuals of the icon, <code>countryCode</code>, <code>routeType</code>
and eventually the <code>stateCode</code> is in most cases sufficient to determine the type of road
shield. In this case an empty string should be passed.</p>
<p><strong>Note:</strong> Texts that contain a <code>CardinalDirection</code> are currently not supported and may lead
to unexpected results. See <code>LocalizedRoadNumber</code> for more details, it provides texts with
and without a cardinal direction.</p>
<ul>
<li><code>shieldText</code> The text of the road-shield. This is the text which is displayed on the road-shield
in reality. It will be in the output road-shield icon.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">RoadShieldIconProperties(this.routeType, this.countryCode, this.stateCode, this.routeNumberName, this.shieldText);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-roadshieldiconproperties-class</li>
<li class="self-crumb">RoadShieldIconProperties constructor</li>
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
`
}</HTMLBlock>
