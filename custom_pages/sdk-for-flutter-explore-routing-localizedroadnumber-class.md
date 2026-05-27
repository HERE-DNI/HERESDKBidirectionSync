---
title: "LocalizedRoadNumber class"
slug: "sdk-for-flutter-explore-routing-localizedroadnumber-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocalizedRoadNumber-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/LocalizedRoadNumber-class.html#constructors">Constructors</a></li>
<li><a href="routing/LocalizedRoadNumber/LocalizedRoadNumber.html">LocalizedRoadNumber</a></li>
<li class="section-title">
<a href="routing/LocalizedRoadNumber-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/LocalizedRoadNumber/direction.html">direction</a></li>
<li><a href="routing/LocalizedRoadNumber/hashCode.html">hashCode</a></li>
<li><a href="routing/LocalizedRoadNumber/localizedNumber.html">localizedNumber</a></li>
<li><a href="routing/LocalizedRoadNumber/routeType.html">routeType</a></li>
<li class="inherited"><a href="routing/LocalizedRoadNumber/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="routing/LocalizedRoadNumber-class.html#instance-methods">Methods</a></li>
<li><a href="routing/LocalizedRoadNumber/getTextWithDirection.html">getTextWithDirection</a></li>
<li class="inherited"><a href="routing/LocalizedRoadNumber/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/LocalizedRoadNumber/toString.html">toString</a></li>
<li class="section-title"><a href="routing/LocalizedRoadNumber-class.html#operators">Operators</a></li>
<li><a href="routing/LocalizedRoadNumber/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li class="self-crumb">LocalizedRoadNumber class</li>
</ol>
<div class="self-name">LocalizedRoadNumber</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/LocalizedRoadNumber-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>LocalizedRoadNumber class</h1></div>
<section class="desc markdown">
<p>Used to represent road number localized to specific language with optional direction and route type information.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="LocalizedRoadNumber">
/sdk-for-flutter-explore-routing-localizedroadnumber-localizedroadnumber(/sdk-for-flutter-explore-core-localizedtext-class localizedNumber, /sdk-for-flutter-explore-core-routetype routeType)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="direction">
/sdk-for-flutter-explore-routing-localizedroadnumber-direction
↔ /sdk-for-flutter-explore-core-cardinaldirection?
</dt>
<dd>
  Road direction.
This property indicates the official directional identifier assigned to highways.
Can be <code>null</code> when direction is not assigned to highways.
The direction indicates the same information as on the signpost shield: For example, if is "101 West", the directions contains WEST.
Note that the official direction is not necessarily the travel direction.
For example, US-101 through the city of Sunnyvale is physically located East to West.
However, the official direction on sign is North/South.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-routing-localizedroadnumber-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="localizedNumber">
/sdk-for-flutter-explore-routing-localizedroadnumber-localizednumber
↔ /sdk-for-flutter-explore-core-localizedtext-class
</dt>
<dd>
  Road number with locale information.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="routeType">
/sdk-for-flutter-explore-routing-localizedroadnumber-routetype
↔ /sdk-for-flutter-explore-core-routetype
</dt>
<dd>
  The route type of the LocalizedRoadNumber.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-routing-localizedroadnumber-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="getTextWithDirection">
/sdk-for-flutter-explore-routing-localizedroadnumber-gettextwithdirection(<wbr/>)
    → String

</dt>
<dd>
  Returns the whole road number information including its cardinal direction.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-routing-localizedroadnumber-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-routing-localizedroadnumber-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
/sdk-for-flutter-explore-routing-localizedroadnumber-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

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
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li class="self-crumb">LocalizedRoadNumber class</li>
</ol>
<h5>routing library</h5>
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
