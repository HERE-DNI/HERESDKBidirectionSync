---
title: "TMCData class"
slug: "sdk-for-flutter-navigate-trafficbroadcast-tmcdata-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TMCData-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="trafficbroadcast/TMCData-class.html#constructors">Constructors</a></li>
<li><a href="trafficbroadcast/TMCData/TMCData.html">TMCData</a></li>
<li class="section-title">
<a href="trafficbroadcast/TMCData-class.html#instance-properties">Properties</a>
</li>
<li><a href="trafficbroadcast/TMCData/additionalEvents.html">additionalEvents</a></li>
<li><a href="trafficbroadcast/TMCData/additionalLocations.html">additionalLocations</a></li>
<li><a href="trafficbroadcast/TMCData/direction.html">direction</a></li>
<li><a href="trafficbroadcast/TMCData/diversionAdvice.html">diversionAdvice</a></li>
<li><a href="trafficbroadcast/TMCData/durationPersistence.html">durationPersistence</a></li>
<li><a href="trafficbroadcast/TMCData/event.html">event</a></li>
<li><a href="trafficbroadcast/TMCData/extent.html">extent</a></li>
<li class="inherited"><a href="trafficbroadcast/TMCData/hashCode.html">hashCode</a></li>
<li><a href="trafficbroadcast/TMCData/location.html">location</a></li>
<li><a href="trafficbroadcast/TMCData/numberOfGroups.html">numberOfGroups</a></li>
<li class="inherited"><a href="trafficbroadcast/TMCData/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="trafficbroadcast/TMCData-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="trafficbroadcast/TMCData/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="trafficbroadcast/TMCData/toString.html">toString</a></li>
<li class="section-title inherited"><a href="trafficbroadcast/TMCData-class.html#operators">Operators</a></li>
<li class="inherited"><a href="trafficbroadcast/TMCData/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-library</li>
<li class="self-crumb">TMCData class</li>
</ol>
<div class="self-name">TMCData</div>
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
<div class="main-content" data-above-sidebar="trafficbroadcast/trafficbroadcast-library-sidebar.html" data-below-sidebar="trafficbroadcast/TMCData-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TMCData class</h1></div>
<section class="desc markdown">
<p>Represents the traffic events in RDS-TMC format.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TMCData">
/sdk-for-flutter-navigate-trafficbroadcast-tmcdata-tmcdata(int numberOfGroups, int extent, int direction, int diversionAdvice, int durationPersistence, int event, int location, List&lt;<wbr/>int&gt; additionalEvents, List&lt;<wbr/>int&gt; additionalLocations)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="additionalEvents">
/sdk-for-flutter-navigate-trafficbroadcast-tmcdata-additionalevents
↔ List&lt;<wbr/>int&gt;
</dt>
<dd>
  Additional traffic events.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="additionalLocations">
/sdk-for-flutter-navigate-trafficbroadcast-tmcdata-additionallocations
↔ List&lt;<wbr/>int&gt;
</dt>
<dd>
  Additional traffic locations.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="direction">
/sdk-for-flutter-navigate-trafficbroadcast-tmcdata-direction
↔ int
</dt>
<dd>
  Street direction.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="diversionAdvice">
/sdk-for-flutter-navigate-trafficbroadcast-tmcdata-diversionadvice
↔ int
</dt>
<dd>
  Diversion advice.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="durationPersistence">
/sdk-for-flutter-navigate-trafficbroadcast-tmcdata-durationpersistence
↔ int
</dt>
<dd>
  Duration persitence.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="event">
/sdk-for-flutter-navigate-trafficbroadcast-tmcdata-event
↔ int
</dt>
<dd>
  Traffic event data.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="extent">
/sdk-for-flutter-navigate-trafficbroadcast-tmcdata-extent
↔ int
</dt>
<dd>
  Extent.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-trafficbroadcast-tmcdata-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="location">
/sdk-for-flutter-navigate-trafficbroadcast-tmcdata-location
↔ int
</dt>
<dd>
  Traffic event location.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="numberOfGroups">
/sdk-for-flutter-navigate-trafficbroadcast-tmcdata-numberofgroups
↔ int
</dt>
<dd>
  Number of groups (1 to 5).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-trafficbroadcast-tmcdata-runtimetype
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
/sdk-for-flutter-navigate-trafficbroadcast-tmcdata-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-trafficbroadcast-tmcdata-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-trafficbroadcast-tmcdata-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-library</li>
<li class="self-crumb">TMCData class</li>
</ol>
<h5>trafficbroadcast library</h5>
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
