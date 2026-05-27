---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-isolineoptionscalculation-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- IsolineOptionsCalculation-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/IsolineOptionsCalculation-class.html#constructors">Constructors</a></li>
<li><a href="routing/IsolineOptionsCalculation/IsolineOptionsCalculation.withDefaults.html">withDefaults</a></li>
<li><a href="routing/IsolineOptionsCalculation/IsolineOptionsCalculation.withDefaultsAndCalculationMode.html">withDefaultsAndCalculationMode</a></li>
<li><a href="routing/IsolineOptionsCalculation/IsolineOptionsCalculation.withDefaultsAndDirection.html">withDefaultsAndDirection</a></li>
<li><a href="routing/IsolineOptionsCalculation/IsolineOptionsCalculation.withNoDefaults.html">withNoDefaults</a></li>
<li class="section-title">
<a href="routing/IsolineOptionsCalculation-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="routing/IsolineOptionsCalculation/hashCode.html">hashCode</a></li>
<li><a href="routing/IsolineOptionsCalculation/isolineCalculationMode.html">isolineCalculationMode</a></li>
<li><a href="routing/IsolineOptionsCalculation/isolineDirection.html">isolineDirection</a></li>
<li><a href="routing/IsolineOptionsCalculation/maxPoints.html">maxPoints</a></li>
<li><a href="routing/IsolineOptionsCalculation/rangeType.html">rangeType</a></li>
<li><a href="routing/IsolineOptionsCalculation/rangeValues.html">rangeValues</a></li>
<li class="inherited"><a href="routing/IsolineOptionsCalculation/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="routing/IsolineOptionsCalculation-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/IsolineOptionsCalculation/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/IsolineOptionsCalculation/toString.html">toString</a></li>
<li class="section-title inherited"><a href="routing/IsolineOptionsCalculation-class.html#operators">Operators</a></li>
<li class="inherited"><a href="routing/IsolineOptionsCalculation/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
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
<p>Setting at least one limit to <a href="../routing/IsolineOptionsCalculation/rangeValues.html">/sdk-for-flutter-explore-routing-isolineoptionscalculation-rangevalues</a> is mandatory or the calculation will fail.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="IsolineOptionsCalculation.withDefaults">
<a href="../routing/IsolineOptionsCalculation/IsolineOptionsCalculation.withDefaults.html">/sdk-for-flutter-explore-routing-isolineoptionscalculation-isolineoptionscalculation-withdefaults</a>(<a href="../routing/IsolineRangeType.html">/sdk-for-flutter-explore-routing-isolinerangetype</a> rangeType, List&lt;<wbr/>int&gt; rangeValues)
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
<a href="../routing/IsolineOptionsCalculation/IsolineOptionsCalculation.withDefaultsAndCalculationMode.html">/sdk-for-flutter-explore-routing-isolineoptionscalculation-isolineoptionscalculation-withdefaultsandcalculationmode</a>(<a href="../routing/IsolineRangeType.html">/sdk-for-flutter-explore-routing-isolinerangetype</a> rangeType, List&lt;<wbr/>int&gt; rangeValues, <a href="../routing/IsolineCalculationMode.html">/sdk-for-flutter-explore-routing-isolinecalculationmode</a> isolineCalculationMode)
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
<a href="../routing/IsolineOptionsCalculation/IsolineOptionsCalculation.withDefaultsAndDirection.html">/sdk-for-flutter-explore-routing-isolineoptionscalculation-isolineoptionscalculation-withdefaultsanddirection</a>(<a href="../routing/IsolineRangeType.html">/sdk-for-flutter-explore-routing-isolinerangetype</a> rangeType, List&lt;<wbr/>int&gt; rangeValues, <a href="../routing/RoutePlaceDirection.html">/sdk-for-flutter-explore-routing-routeplacedirection</a> isolineDirection)
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
<a href="../routing/IsolineOptionsCalculation/IsolineOptionsCalculation.withNoDefaults.html">/sdk-for-flutter-explore-routing-isolineoptionscalculation-isolineoptionscalculation-withnodefaults</a>(<a href="../routing/IsolineRangeType.html">/sdk-for-flutter-explore-routing-isolinerangetype</a> rangeType, List&lt;<wbr/>int&gt; rangeValues, <a href="../routing/IsolineCalculationMode.html">/sdk-for-flutter-explore-routing-isolinecalculationmode</a> isolineCalculationMode, int? maxPoints, <a href="../routing/RoutePlaceDirection.html">/sdk-for-flutter-explore-routing-routeplacedirection</a> isolineDirection)
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
<a href="../routing/IsolineOptionsCalculation/hashCode.html">/sdk-for-flutter-explore-routing-isolineoptionscalculation-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="isolineCalculationMode">
<a href="../routing/IsolineOptionsCalculation/isolineCalculationMode.html">/sdk-for-flutter-explore-routing-isolineoptionscalculation-isolinecalculationmode</a>
↔ <a href="../routing/IsolineCalculationMode.html">/sdk-for-flutter-explore-routing-isolinecalculationmode</a>
</dt>
<dd>
  Specifies how isoline calculation is optimized.
The default waypoint type is <a href="../routing/IsolineCalculationMode.html">/sdk-for-flutter-explore-routing-isolinecalculationmode</a>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isolineDirection">
<a href="../routing/IsolineOptionsCalculation/isolineDirection.html">/sdk-for-flutter-explore-routing-isolineoptionscalculation-isolinedirection</a>
↔ <a href="../routing/RoutePlaceDirection.html">/sdk-for-flutter-explore-routing-routeplacedirection</a>
</dt>
<dd>
  Specifies if calculations will be from or to a specific point.
The default isoline direction is <a href="../routing/RoutePlaceDirection.html">/sdk-for-flutter-explore-routing-routeplacedirection</a>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxPoints">
<a href="../routing/IsolineOptionsCalculation/maxPoints.html">/sdk-for-flutter-explore-routing-isolineoptionscalculation-maxpoints</a>
↔ int?
</dt>
<dd>
  Limits the number of points in the resulting isoline polygon. If the
isoline consists of multiple polygons, the sum of points from all
polygons is considered. Note that this parameter does not affect the calculation,
but the shape of the polygon. Look at <a href="../routing/IsolineCalculationMode.html">/sdk-for-flutter-explore-routing-isolinecalculationmode</a> parameter
to optimize performance.
A higher value will result in a more accurate polygon shape. Rendering a polygon
with a high number of points can negatively impact rendering performance.
The minimum allowed value is 30, lower values will be ignored.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="rangeType">
<a href="../routing/IsolineOptionsCalculation/rangeType.html">/sdk-for-flutter-explore-routing-isolineoptionscalculation-rangetype</a>
↔ <a href="../routing/IsolineRangeType.html">/sdk-for-flutter-explore-routing-isolinerangetype</a>
</dt>
<dd>
  Specifies the range of values to be included in the isoline.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="rangeValues">
<a href="../routing/IsolineOptionsCalculation/rangeValues.html">/sdk-for-flutter-explore-routing-isolineoptionscalculation-rangevalues</a>
↔ List&lt;<wbr/>int&gt;
</dt>
<dd>
  A list of ranges. The unit is defined by the type parameter.
Each range defines the maximum allowed value to reach a destination.
For each value an <a href="../routing/Isoline-class.html">/sdk-for-flutter-explore-routing-isoline-class</a> is calculated indicating the reachable area.
If empty, <a href="../routing/IsolineOptions-class.html">/sdk-for-flutter-explore-routing-isolineoptions-class</a> object is considered invalid.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/IsolineOptionsCalculation/runtimeType.html">/sdk-for-flutter-explore-routing-isolineoptionscalculation-runtimetype</a>
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
<a href="../routing/IsolineOptionsCalculation/noSuchMethod.html">/sdk-for-flutter-explore-routing-isolineoptionscalculation-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/IsolineOptionsCalculation/toString.html">/sdk-for-flutter-explore-routing-isolineoptionscalculation-tostring</a>(<wbr/>)
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
<a href="../routing/IsolineOptionsCalculation/operator_equals.html">/sdk-for-flutter-explore-routing-isolineoptionscalculation-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
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
</div></div>
</div>
</HTMLBlock>
