---
title: "Untitled"
slug: "sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficBroadcast-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-library</li>
<li class="self-crumb">TrafficBroadcast class</li>
</ol>
<div class="self-name">TrafficBroadcast</div>
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
<div class="main-content" data-above-sidebar="trafficbroadcast/trafficbroadcast-library-sidebar.html" data-below-sidebar="trafficbroadcast/TrafficBroadcast-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TrafficBroadcast class abstract</h1></div>
<section class="desc markdown">
<p>A <code>TrafficBroadcast</code> is expecting the <a href="https://en.wikipedia.org/wiki/Traffic_message_channel">RDS-TMC</a>
format and it can be used when there is no internet connection, so that the <code>OfflineRoutingEngine</code>
can utilize traffic data coming over a radio channel.</p>
<p>The /sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-activate method needs to be called to
receive traffic data events.</p>
<p><strong>Note:</strong> In order to adopt the <code>TrafficDataProvider</code> interface special hardware is required. Talk
to your HERE representative for more details. Only by adopting the <code>TrafficDataProvider</code> interface
you can integrate radio station signals providing traffic broadcasts. Traffic broadcasts are meant
to be used <em>independently</em> from the already included traffic on routes, on the map and from the
HERE backends (when using the <code>TrafficEngine</code>).</p>
<p>This class continuously reacts to new locations provided from a location source and acts as a
/sdk-for-flutter-navigate-core-locationlistener-class. The location must be updated regardless of calling /sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-activate.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implemented types</dt>
<dd>
<ul class="comma-separated clazz-relationships">
<li>/sdk-for-flutter-navigate-core-locationlistener-class</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TrafficBroadcast">
/sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-trafficbroadcast(/sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcastparameters-class parameters)
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="TrafficBroadcast.withSdkEngine">
/sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-trafficbroadcast-withsdkengine(/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine, /sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcastparameters-class parameters)
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-core-locationlistener-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-core-locationlistener-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="trafficDataProvider">
/sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-trafficdataprovider
→ /sdk-for-flutter-navigate-traffic-trafficdataprovider-class?
</dt>
<dd>
  The traffic data provider that provides the traffic information.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="activate">
/sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-activate(<wbr/>)
    → void

</dt>
<dd>
  Activates the reception of traffic data over the radio channel.
  

</dd>
<dt class="callable" id="deactivate">
/sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-deactivate(<wbr/>)
    → void

</dt>
<dd>
  Deactivates the reception of traffic data over the radio channel.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-core-locationlistener-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="onLocationUpdated">
/sdk-for-flutter-navigate-core-locationlistener-onlocationupdated(<wbr/>/sdk-for-flutter-navigate-core-location-class location)
    → void

</dt>
<dd class="inherited">
  Called each time a new location is available.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="onTMCDataUpdated">
/sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-ontmcdataupdated(<wbr/>/sdk-for-flutter-navigate-trafficbroadcast-tmcdata-class tmcData)
    → void

</dt>
<dd>
  Must be called on every TMC data update.
  

</dd>
<dt class="callable" id="onTMCServiceProviderInfoUpdated">
/sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-ontmcserviceproviderinfoupdated(<wbr/>/sdk-for-flutter-navigate-trafficbroadcast-tmcserviceproviderinfo-class tmcServiceProdiverInfo)
    → void

</dt>
<dd>
  Must be called on every TMC service prodiver info update.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-core-locationlistener-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-core-locationlistener-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">TrafficBroadcast class</li>
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



</div>
`
}</HTMLBlock>
