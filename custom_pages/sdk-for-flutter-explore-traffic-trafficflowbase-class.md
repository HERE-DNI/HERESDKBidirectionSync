---
title: "Constructors"
slug: "sdk-for-flutter-explore-traffic-trafficflowbase-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- TrafficFlowBase-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="traffic/TrafficFlowBase-class.html#constructors">Constructors</a></li>
<li><a href="traffic/TrafficFlowBase/TrafficFlowBase.html">TrafficFlowBase</a></li>
<li class="section-title">
<a href="traffic/TrafficFlowBase-class.html#instance-properties">Properties</a>
</li>
<li><a href="traffic/TrafficFlowBase/freeFlowSpeedInMetersPerSecond.html">freeFlowSpeedInMetersPerSecond</a></li>
<li class="inherited"><a href="traffic/TrafficFlowBase/hashCode.html">hashCode</a></li>
<li><a href="traffic/TrafficFlowBase/jamFactor.html">jamFactor</a></li>
<li class="inherited"><a href="traffic/TrafficFlowBase/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="traffic/TrafficFlowBase-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="traffic/TrafficFlowBase/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="traffic/TrafficFlowBase/toString.html">toString</a></li>
<li class="section-title inherited"><a href="traffic/TrafficFlowBase-class.html#operators">Operators</a></li>
<li class="inherited"><a href="traffic/TrafficFlowBase/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../traffic/traffic-library.html">/sdk-for-flutter-explore-traffic-traffic-library</a></li>
<li class="self-crumb">TrafficFlowBase class</li>
</ol>
<div class="self-name">TrafficFlowBase</div>
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
<div class="main-content" data-above-sidebar="traffic/traffic-library-sidebar.html" data-below-sidebar="traffic/TrafficFlowBase-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TrafficFlowBase class abstract</h1></div>
<section class="desc markdown">
<p>This interface provides details about a traffic flow.<br/>
For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implementers</dt>
<dd><ul class="comma-separated clazz-relationships">
<li><a href="../traffic/TrafficFlow-class.html">/sdk-for-flutter-explore-traffic-trafficflow-class</a></li>
</ul></dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TrafficFlowBase">
<a href="../traffic/TrafficFlowBase/TrafficFlowBase.html">/sdk-for-flutter-explore-traffic-trafficflowbase-trafficflowbase</a>(double freeFlowSpeedInMetersPerSecondGetLambda(), double jamFactorGetLambda())
</dt>
<dd>
          This interface provides details about a traffic flow.<br/>
For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="freeFlowSpeedInMetersPerSecond">
<a href="../traffic/TrafficFlowBase/freeFlowSpeedInMetersPerSecond.html">/sdk-for-flutter-explore-traffic-trafficflowbase-freeflowspeedinmeterspersecond</a>
→ double
</dt>
<dd>
  The reference speed in meters per second along the roadway when no traffic is present.
Gets the reference speed in meters per second along the roadway when no traffic is present.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
<a href="../traffic/TrafficFlowBase/hashCode.html">/sdk-for-flutter-explore-traffic-trafficflowbase-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="jamFactor">
<a href="../traffic/TrafficFlowBase/jamFactor.html">/sdk-for-flutter-explore-traffic-trafficflowbase-jamfactor</a>
→ double
</dt>
<dd>
  A value for the amount of traffic on the roadway.
The value, between 0.0 and 10.0, indicate the expected quality of travel.
A value of 0.0 indicates that there is no congestion on the roadway.
As the value approaches 10.0, it indicates increasing congestion.
A value of 10.0 is reserved to represent a blocked roadway (closure).
Gets a value for the amount of traffic on the roadway.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../traffic/TrafficFlowBase/runtimeType.html">/sdk-for-flutter-explore-traffic-trafficflowbase-runtimetype</a>
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
<a href="../traffic/TrafficFlowBase/noSuchMethod.html">/sdk-for-flutter-explore-traffic-trafficflowbase-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../traffic/TrafficFlowBase/toString.html">/sdk-for-flutter-explore-traffic-trafficflowbase-tostring</a>(<wbr/>)
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
<a href="../traffic/TrafficFlowBase/operator_equals.html">/sdk-for-flutter-explore-traffic-trafficflowbase-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../traffic/traffic-library.html">/sdk-for-flutter-explore-traffic-traffic-library</a></li>
<li class="self-crumb">TrafficFlowBase class</li>
</ol>
<h5>traffic library</h5>
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
