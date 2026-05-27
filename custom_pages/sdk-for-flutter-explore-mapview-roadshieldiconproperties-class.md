---
title: "RoadShieldIconProperties class"
slug: "sdk-for-flutter-explore-mapview-roadshieldiconproperties-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoadShieldIconProperties-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/RoadShieldIconProperties-class.html#constructors">Constructors</a></li>
<li><a href="mapview/RoadShieldIconProperties/RoadShieldIconProperties.html">RoadShieldIconProperties</a></li>
<li class="section-title">
<a href="mapview/RoadShieldIconProperties-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview/RoadShieldIconProperties/countryCode.html">countryCode</a></li>
<li class="inherited"><a href="mapview/RoadShieldIconProperties/hashCode.html">hashCode</a></li>
<li><a href="mapview/RoadShieldIconProperties/routeNumberName.html">routeNumberName</a></li>
<li><a href="mapview/RoadShieldIconProperties/routeType.html">routeType</a></li>
<li class="inherited"><a href="mapview/RoadShieldIconProperties/runtimeType.html">runtimeType</a></li>
<li><a href="mapview/RoadShieldIconProperties/shieldText.html">shieldText</a></li>
<li><a href="mapview/RoadShieldIconProperties/stateCode.html">stateCode</a></li>
<li class="section-title inherited"><a href="mapview/RoadShieldIconProperties-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/RoadShieldIconProperties/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/RoadShieldIconProperties/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/RoadShieldIconProperties-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/RoadShieldIconProperties/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">RoadShieldIconProperties class</li>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/RoadShieldIconProperties-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RoadShieldIconProperties class</h1></div>
<section class="desc markdown">
<p>Contains the information required to create a road shield image.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RoadShieldIconProperties">
/sdk-for-flutter-explore-mapview-roadshieldiconproperties-roadshieldiconproperties(/sdk-for-flutter-explore-core-routetype routeType, String countryCode, String stateCode, String routeNumberName, String shieldText)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="countryCode">
/sdk-for-flutter-explore-mapview-roadshieldiconproperties-countrycode
↔ String
</dt>
<dd>
  The country code in ISO-3166-1 alpha-3 format, which will determine the type of road shield.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-mapview-roadshieldiconproperties-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="routeNumberName">
/sdk-for-flutter-explore-mapview-roadshieldiconproperties-routenumbername
↔ String
</dt>
<dd>
  A string that is used to additionally determine the road shield's visual representation.
In a routing context, the text can be taken from a <code>LocalizedRoadNumber</code>, which
is available for each <code>Span</code> of a <code>Route</code> object.
Typically, the string contains the number of a road, such as "E100". Internally, the text
is parsed with a RegEx pattern and the results will be used along with other properties
such as <code>routeType</code>, <code>countryCode</code> and <code>stateCode</code> to identify the visual representation
of a road shield icon.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="routeType">
/sdk-for-flutter-explore-mapview-roadshieldiconproperties-routetype
↔ /sdk-for-flutter-explore-core-routetype
</dt>
<dd>
  The type of route indicating the significance of the road in a range from 0 to 6. A value of
1 stands for the most major route and 6 the most minor, with 0 being of unknown type.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-mapview-roadshieldiconproperties-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="shieldText">
/sdk-for-flutter-explore-mapview-roadshieldiconproperties-shieldtext
↔ String
</dt>
<dd>
  The text of the road-shield. This is the text which is displayed on the road-shield
in reality. It will be in the output road-shield icon.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="stateCode">
/sdk-for-flutter-explore-mapview-roadshieldiconproperties-statecode
↔ String
</dt>
<dd>
  The state code for the road. It's a 2-letter code in ISO 3166-2 format. For example
the ones listed for US on this page <a href="https://en.wikipedia.org/wiki/ISO_3166-2:US">https://en.wikipedia.org/wiki/ISO_3166-2:US</a>.
The code "AL" is for Alabama. Another example is the code for autonomous
communities listed on <a href="https://en.wikipedia.org/wiki/ISO_3166-2:ES">https://en.wikipedia.org/wiki/ISO_3166-2:ES</a>. Can be empty if
not required for the particular country.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-mapview-roadshieldiconproperties-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-mapview-roadshieldiconproperties-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-explore-mapview-roadshieldiconproperties-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">RoadShieldIconProperties class</li>
</ol>
<h5>mapview library</h5>
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
