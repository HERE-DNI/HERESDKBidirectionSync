---
title: "Untitled"
slug: "sdk-for-flutter-navigate-venue-venueengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueEngine-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-venue-venue-library</li>
<li class="self-crumb">VenueEngine class</li>
</ol>
<div class="self-name">VenueEngine</div>
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
<div class="main-content" data-above-sidebar="venue/venue-library-sidebar.html" data-below-sidebar="venue/VenueEngine-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>VenueEngine class abstract</h1></div>
<section class="desc markdown">
<p>VenueEngine is an add-on to the base map functionality with its
own content loading and cache.</p>
<p>VenueEngine gives access to the venue functionality, which allows you
to load and visualize venues on the map, search content inside venues etc.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="VenueEngine">
/sdk-for-flutter-navigate-venue-venueengine-venueengine(/sdk-for-flutter-navigate-venue-venueengineinitcallback? callback)
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="VenueEngine.withSdkEngine">
/sdk-for-flutter-navigate-venue-venueengine-venueengine-withsdkengine(/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine, /sdk-for-flutter-navigate-venue-venueengineinitcallback? callback)
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
/sdk-for-flutter-navigate-venue-venueengine-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-venue-venueengine-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="venueMap">
/sdk-for-flutter-navigate-venue-venueengine-venuemap
→ /sdk-for-flutter-navigate-venue-control-venuemap-class
</dt>
<dd>
  The venue map.
Gets a venue map to visualize venues and control the
state of the venues on the map. You need to start the /sdk-for-flutter-navigate-venue-service-venueservice-class to
be able to load venues.
Gets a venue map to visualize venues.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="venueService">
/sdk-for-flutter-navigate-venue-venueengine-venueservice
→ /sdk-for-flutter-navigate-venue-service-venueservice-class
</dt>
<dd>
  The venue service.
Gets the /sdk-for-flutter-navigate-venue-service-venueservice-class. This service
can be used to load the /sdk-for-flutter-navigate-venue-data-venuemodel-class objects.
Gets the venue service. This service can be used to load the venue model objects.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="destroy">
/sdk-for-flutter-navigate-venue-venueengine-destroy(<wbr/>)
    → void

</dt>
<dd>
  Releases all internally used resources.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-venue-venueengine-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="start">
/sdk-for-flutter-navigate-venue-venueengine-start(<wbr/>/sdk-for-flutter-navigate-core-authenticationcallback? callback)
    → void

</dt>
<dd>
  Authenticates asynchronously using HERE SDK credentials and uses a result token to start
the /sdk-for-flutter-navigate-venue-service-venueservice-class.
  

</dd>
<dt class="callable" id="startWithToken">
/sdk-for-flutter-navigate-venue-venueengine-startwithtoken(<wbr/>String token)
    → void

</dt>
<dd>
  Authenticates asynchronously using HERE SDK credentials using a token to start
the /sdk-for-flutter-navigate-venue-service-venueservice-class.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-venue-venueengine-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-venue-venueengine-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-venue-venue-library</li>
<li class="self-crumb">VenueEngine class</li>
</ol>
<h5>venue library</h5>
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
