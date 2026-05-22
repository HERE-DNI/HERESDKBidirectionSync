---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficMergeWarningListener-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">TrafficMergeWarningListener class</li>
</ol>
<div class="self-name">TrafficMergeWarningListener</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/TrafficMergeWarningListener-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TrafficMergeWarningListener class abstract</h1></div>
<section class="desc markdown">
<p>This abstract class
should be implemented in order to receive traffic merge warnings.</p>
<p><strong>Note:</strong> The traffic merge warner is a point warner, which means that for a traffic merge there will <em>always</em> be
2 warnings emitted, with the <code>TrafficMergeWarning.distance_type</code> set to <code>DistanceType.AHEAD</code> and <code>DistanceType.PASSED</code>
which is given when the location of the traffic merge is reached.
A <code>TrafficMergeWarning</code> will not be given until the previous warning of that type has been passed.
For example, a route with <code>TrafficMergeWarning</code> 120 meters and <code>TrafficMergeWarning</code> 160 meters ahead,
the first <code>TrafficMergeWarning.distance_to_traffic_merge_in_meters</code> is 120 meters
and the next <code>TrafficMergeWarning.distance_to_traffic_merge_in_meters</code> is then 40 meters,
since that is the distance between the first and second warnings.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TrafficMergeWarningListener">
/sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-trafficmergewarninglistener(void onTrafficMergeWarningUpdatedLambda(/sdk-for-flutter-navigate-navigation-trafficmergewarning-class))
</dt>
<dd>
          This abstract class
should be implemented in order to receive traffic merge warnings.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-runtimetype
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
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="onTrafficMergeWarningUpdated">
/sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-ontrafficmergewarningupdated(<wbr/>/sdk-for-flutter-navigate-navigation-trafficmergewarning-class trafficMergeWarning)
    → void

</dt>
<dd>
  Called whenever a new traffic merge warning is available.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">TrafficMergeWarningListener class</li>
</ol>
<h5>navigation library</h5>
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
