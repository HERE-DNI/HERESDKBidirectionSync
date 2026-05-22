---
title: "Untitled"
slug: "sdk-for-flutter-navigate-search-myplaces-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MyPlaces-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li class="self-crumb">MyPlaces class</li>
</ol>
<div class="self-name">MyPlaces</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/MyPlaces-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MyPlaces class abstract</h1></div>
<section class="desc markdown">
<p>Provides means to populate personal places data source.</p>
<p>Also acts as a
owner of the collection of personal places. MyPlaces is
memory-only object: nothing is persisted and/or sent over the network.
Client has full control on how to store personal places.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MyPlaces">
/sdk-for-flutter-navigate-search-myplaces-myplaces()
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
/sdk-for-flutter-navigate-search-myplaces-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="places">
/sdk-for-flutter-navigate-search-myplaces-places
→ List&lt;<wbr/>/sdk-for-flutter-navigate-search-geoplace-class&gt;
</dt>
<dd>
  The list of places which currently belong to this data source. This list is
a clone of the internal list and thus changing it has no effect on the data source.
Gets the list of places which currently belongs to this data source. The returned list is
a clone of the internal list and thus changing it has no effect on the data source.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-search-myplaces-runtimetype
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
<dt class="callable" id="addPlace">
/sdk-for-flutter-navigate-search-myplaces-addplace(<wbr/>/sdk-for-flutter-navigate-search-geoplace-class place, /sdk-for-flutter-navigate-core-threading-ontaskcompleted callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Adds a place to this data source.
  

</dd>
<dt class="callable" id="addPlaces">
/sdk-for-flutter-navigate-search-myplaces-addplaces(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-search-geoplace-class&gt; places, /sdk-for-flutter-navigate-core-threading-ontaskcompleted callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Adds a list of places to this data source.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-search-myplaces-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="removeAll">
/sdk-for-flutter-navigate-search-myplaces-removeall(<wbr/>/sdk-for-flutter-navigate-core-threading-ontaskcompleted callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Removes all places from this data source.
  

</dd>
<dt class="callable" id="removePlace">
/sdk-for-flutter-navigate-search-myplaces-removeplace(<wbr/>String placeId, /sdk-for-flutter-navigate-core-threading-ontaskcompleted callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Removes a place from this data source.
  

</dd>
<dt class="callable" id="removePlaces">
/sdk-for-flutter-navigate-search-myplaces-removeplaces(<wbr/>List&lt;<wbr/>String&gt; placeIds, /sdk-for-flutter-navigate-core-threading-ontaskcompleted callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Removes a list of places from this data source.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-search-myplaces-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-search-myplaces-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li class="self-crumb">MyPlaces class</li>
</ol>
<h5>search library</h5>
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
