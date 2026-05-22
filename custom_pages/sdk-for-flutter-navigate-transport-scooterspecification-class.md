---
title: "Untitled"
slug: "sdk-for-flutter-navigate-transport-scooterspecification-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ScooterSpecification-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-transport-transport-library</li>
<li class="self-crumb">ScooterSpecification class</li>
</ol>
<div class="self-name">ScooterSpecification</div>
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
<div class="main-content" data-above-sidebar="transport/transport-library-sidebar.html" data-below-sidebar="transport/ScooterSpecification-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>ScooterSpecification class</h1></div>
<section class="desc markdown">
<p>Scooter specific settings.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="ScooterSpecification">
/sdk-for-flutter-navigate-transport-scooterspecification-scooterspecification()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="allowScooterOnHighway">
/sdk-for-flutter-navigate-transport-scooterspecification-allowscooteronhighway
↔ bool
</dt>
<dd>
  Specifies whether scooter is allowed on highway or not. <code>True</code> means scooter is
allowed to use highways and <code>false</code> means otherwise.
Defaults to <code>false</code>.
Note that there is a similar parameter in <code>AvoidanceOptions</code>, to disallow highway usage,
see <code>RoadFeatures.CONTROLLED_ACCESS_HIGHWAY</code>.
As the avoidance options takes precedence, if this parameter is also used, then
scooters are not allowed to use highways even if <code>allowHighway</code> is set to <code>true</code>.
However, if no alternative route is possible, the calculated route may use highways.
In such a case, a <code>SectionNotice</code> will be provided in the related <code>Section</code> to indicate that
the highway usage restriction is violated on this route.
A few examples:
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-transport-scooterspecification-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-transport-scooterspecification-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-transport-scooterspecification-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-transport-scooterspecification-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-transport-scooterspecification-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-transport-transport-library</li>
<li class="self-crumb">ScooterSpecification class</li>
</ol>
<h5>transport library</h5>
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
