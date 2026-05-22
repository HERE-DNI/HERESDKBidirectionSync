---
title: "Untitled"
slug: "sdk-for-flutter-explore-transport-carspecifications-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CarSpecifications-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-transport-transport-library</li>
<li class="self-crumb">CarSpecifications class</li>
</ol>
<div class="self-name">CarSpecifications</div>
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
<div class="main-content" data-above-sidebar="transport/transport-library-sidebar.html" data-below-sidebar="transport/CarSpecifications-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>CarSpecifications class</h1></div>
<section class="desc markdown">
<p>Car specifications contain vehicle related attributes.</p>
<p>Examples: Dimensions, weight, axle count.
Only the fields that are set are considered for restriction handling.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Annotations</dt>
<dd>
<ul class="annotation-list clazz-relationships">
<li>@Deprecated("Will be removed in v4.28.0. Use <code>TransportSpecification</code> instead.")</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="CarSpecifications">
/sdk-for-flutter-explore-transport-carspecifications-carspecifications([int? grossWeightInKilograms = null, int? heightInCentimeters = null, int? widthInCentimeters = null, int? lengthInCentimeters = null, int? axleCount = null, int? trailerCount = null, int? trailerAxleCount = null])
</dt>
<dd>
          Creates a new instance.
        </dd>
<dt class="callable" id="CarSpecifications.withDefaults">
/sdk-for-flutter-explore-transport-carspecifications-carspecifications-withdefaults()
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="axleCount">
/sdk-for-flutter-explore-transport-carspecifications-axlecount
↔ int?
</dt>
<dd>
  Defines total number of axles in the vehicle. The provided value must be greater than or
equal to 2. By default, it is not set.
Route calculation: When not set, possible axle count restrictions will not be
taken into consideration.
When specifying /sdk-for-flutter-explore-transport-carspecifications-traileraxlecount, then /sdk-for-flutter-explore-transport-carspecifications-axlecount is required and must be greater than /sdk-for-flutter-explore-transport-carspecifications-traileraxlecount.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="grossWeightInKilograms">
/sdk-for-flutter-explore-transport-carspecifications-grossweightinkilograms
↔ int?
</dt>
<dd>
  Car weight including trailers and shipped goods in kilograms. The provided value
must be greater than or equal to 0. By default, it is not set.
<strong>Note:</strong>
This parameter is limited to a maximum weight of 4250 kg without trailer and 7550 kg with trailer.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-transport-carspecifications-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="heightInCentimeters">
/sdk-for-flutter-explore-transport-carspecifications-heightincentimeters
↔ int?
</dt>
<dd>
  Car height in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="lengthInCentimeters">
/sdk-for-flutter-explore-transport-carspecifications-lengthincentimeters
↔ int?
</dt>
<dd>
  Car length in centimeters. The provided value must be in the range [0, 30000].
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-transport-carspecifications-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="trailerAxleCount">
/sdk-for-flutter-explore-transport-carspecifications-traileraxlecount
↔ int?
</dt>
<dd>
  Defines total number of axles across all the trailers attached to the vehicle.
This number is included in /sdk-for-flutter-explore-transport-carspecifications-axlecount, hence /sdk-for-flutter-explore-transport-carspecifications-traileraxlecount must be less than /sdk-for-flutter-explore-transport-carspecifications-axlecount
and greater than or equal to 1. /sdk-for-flutter-explore-transport-carspecifications-axlecount and /sdk-for-flutter-explore-transport-carspecifications-trailercount are required to specify /sdk-for-flutter-explore-transport-carspecifications-traileraxlecount.
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="trailerCount">
/sdk-for-flutter-explore-transport-carspecifications-trailercount
↔ int?
</dt>
<dd>
  Defines number of trailers attached to the vehicle. The provided value must be in the range
[0, 1]. By default, it is not set.
When specifying /sdk-for-flutter-explore-transport-carspecifications-traileraxlecount, then /sdk-for-flutter-explore-transport-carspecifications-trailercount is required and must be greater than 0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="widthInCentimeters">
/sdk-for-flutter-explore-transport-carspecifications-widthincentimeters
↔ int?
</dt>
<dd>
  Car width in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-transport-carspecifications-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-transport-carspecifications-tostring(<wbr/>)
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
/sdk-for-flutter-explore-transport-carspecifications-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore-transport-transport-library</li>
<li class="self-crumb">CarSpecifications class</li>
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
