---
title: "Untitled"
slug: "sdk-for-flutter-explore-routing-isolineoptionscalculation-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- IsolineOptionsCalculation-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li class="self-crumb">IsolineOptionsCalculation class</li>
</ol>
<div class="self-name">IsolineOptionsCalculation</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/IsolineOptionsCalculation-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>IsolineOptionsCalculation class</h1></div>
<section class="desc markdown">
<p>Specifies isoline parameters.</p>
<p>Setting at least one limit to /sdk-for-flutter-explore-routing-isolineoptionscalculation-rangevalues is mandatory or the calculation will fail.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="IsolineOptionsCalculation.withDefaults">
/sdk-for-flutter-explore-routing-isolineoptionscalculation-isolineoptionscalculation-withdefaults(/sdk-for-flutter-explore-routing-isolinerangetype rangeType, List&lt;<wbr/>int&gt; rangeValues)
</dt>
<dd>
<li>
<p><code>rangeType</code> The range type.</p>
</li>
<li>
<p><code>rangeValues</code> Range values.</p>
</li>
<div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="IsolineOptionsCalculation.withDefaultsAndCalculationMode">
/sdk-for-flutter-explore-routing-isolineoptionscalculation-isolineoptionscalculation-withdefaultsandcalculationmode(/sdk-for-flutter-explore-routing-isolinerangetype rangeType, List&lt;<wbr/>int&gt; rangeValues, /sdk-for-flutter-explore-routing-isolinecalculationmode isolineCalculationMode)
</dt>
<dd>
<li>
<p><code>rangeType</code> The range type.</p>
</li>
<li>
<p><code>rangeValues</code> Range values.</p>
</li>
<li>
<p><code>isolineCalculationMode</code> The isoline calculation mode.</p>
</li>
<div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="IsolineOptionsCalculation.withDefaultsAndDirection">
/sdk-for-flutter-explore-routing-isolineoptionscalculation-isolineoptionscalculation-withdefaultsanddirection(/sdk-for-flutter-explore-routing-isolinerangetype rangeType, List&lt;<wbr/>int&gt; rangeValues, /sdk-for-flutter-explore-routing-routeplacedirection isolineDirection)
</dt>
<dd>
<li>
<p><code>rangeType</code> The range type.</p>
</li>
<li>
<p><code>rangeValues</code> Range values.</p>
</li>
<li>
<p><code>isolineDirection</code> The isoline direction.</p>
</li>
<div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="IsolineOptionsCalculation.withNoDefaults">
/sdk-for-flutter-explore-routing-isolineoptionscalculation-isolineoptionscalculation-withnodefaults(/sdk-for-flutter-explore-routing-isolinerangetype rangeType, List&lt;<wbr/>int&gt; rangeValues, /sdk-for-flutter-explore-routing-isolinecalculationmode isolineCalculationMode, int? maxPoints, /sdk-for-flutter-explore-routing-routeplacedirection isolineDirection)
</dt>
<dd>
<li>
<p><code>rangeType</code> The range type.</p>
</li>
<li>
<p><code>rangeValues</code> Range values.</p>
</li>
<li>
<p><code>isolineCalculationMode</code> The isoline calculation mode.</p>
</li>
<li>
<p><code>maxPoints</code> The max points number.</p>
</li>
<li>
<p><code>isolineDirection</code> The isoline direction.</p>
</li>
<div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-routing-isolineoptionscalculation-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="isolineCalculationMode">
/sdk-for-flutter-explore-routing-isolineoptionscalculation-isolinecalculationmode
↔ /sdk-for-flutter-explore-routing-isolinecalculationmode
</dt>
<dd>
  Specifies how isoline calculation is optimized.
The default waypoint type is /sdk-for-flutter-explore-routing-isolinecalculationmode.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isolineDirection">
/sdk-for-flutter-explore-routing-isolineoptionscalculation-isolinedirection
↔ /sdk-for-flutter-explore-routing-routeplacedirection
</dt>
<dd>
  Specifies if calculations will be from or to a specific point.
The default isoline direction is /sdk-for-flutter-explore-routing-routeplacedirection.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxPoints">
/sdk-for-flutter-explore-routing-isolineoptionscalculation-maxpoints
↔ int?
</dt>
<dd>
  Limits the number of points in the resulting isoline polygon. If the
isoline consists of multiple polygons, the sum of points from all
polygons is considered. Note that this parameter does not affect the calculation,
but the shape of the polygon. Look at /sdk-for-flutter-explore-routing-isolinecalculationmode parameter
to optimize performance.
A higher value will result in a more accurate polygon shape. Rendering a polygon
with a high number of points can negatively impact rendering performance.
The minimum allowed value is 30, lower values will be ignored.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="rangeType">
/sdk-for-flutter-explore-routing-isolineoptionscalculation-rangetype
↔ /sdk-for-flutter-explore-routing-isolinerangetype
</dt>
<dd>
  Specifies the range of values to be included in the isoline.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="rangeValues">
/sdk-for-flutter-explore-routing-isolineoptionscalculation-rangevalues
↔ List&lt;<wbr/>int&gt;
</dt>
<dd>
  A list of ranges. The unit is defined by the type parameter.
Each range defines the maximum allowed value to reach a destination.
For each value an /sdk-for-flutter-explore-routing-isoline-class is calculated indicating the reachable area.
If empty, /sdk-for-flutter-explore-routing-isolineoptions-class object is considered invalid.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-routing-isolineoptionscalculation-runtimetype
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
/sdk-for-flutter-explore-routing-isolineoptionscalculation-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-routing-isolineoptionscalculation-tostring(<wbr/>)
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
/sdk-for-flutter-explore-routing-isolineoptionscalculation-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li class="self-crumb">IsolineOptionsCalculation class</li>
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



</div>
`
}</HTMLBlock>
