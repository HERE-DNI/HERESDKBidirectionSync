---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-widgetpin-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- WidgetPin-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">WidgetPin class</li>
</ol>
<div class="self-name">WidgetPin</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/WidgetPin-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>WidgetPin class abstract</h1></div>
<section class="desc markdown">
<p>Controller for a <code>Widget</code> pinned at a fixed geographical location on the map.</p>
<p>A pinned Widget tracks the geographical location as the map is being
manipulated. It behaves like a /sdk-for-flutter-navigate-mapview-mapmarker-class, only it's a regular
Flutter Widget and is not part of normal map rendering.</p>
<p>WidgetPin allows modifying the geographical location of the pinned Widget
as well as its placement relative to it.</p>
<p>Use /sdk-for-flutter-navigate-mapview-heremapcontroller-pinwidget to pin (add) a <code>Widget</code> to a map and obtain
in instance of /sdk-for-flutter-navigate-mapview-widgetpin-class that controls it.</p>
<p>To unpin (remove) a Widget from the map, use /sdk-for-flutter-navigate-mapview-heremapcontroller-unpinwidget.
or /sdk-for-flutter-navigate-mapview-widgetpin-unpin.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="WidgetPin">
/sdk-for-flutter-navigate-mapview-widgetpin-widgetpin({required Widget child, required /sdk-for-flutter-navigate-core-geocoordinates-class coordinates, /sdk-for-flutter-navigate-core-anchor2d-class? anchor, dynamic onChange()?, dynamic onUnpin(/sdk-for-flutter-navigate-mapview-widgetpin-class)?})
</dt>
<dd>
          Creates a /sdk-for-flutter-navigate-mapview-widgetpin-class displaying child <code>Widget</code> at coordinates location on the map
Don't use this constructor directly. Instead use /sdk-for-flutter-navigate-mapview-heremapcontroller-pinwidget to create a /sdk-for-flutter-navigate-mapview-widgetpin-class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="anchor">
/sdk-for-flutter-navigate-mapview-widgetpin-anchor
↔ /sdk-for-flutter-navigate-core-anchor2d-class
</dt>
<dd>
  Gets pinned <code>Widget</code>'s placement relative to geographical location,
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="child">
/sdk-for-flutter-navigate-mapview-widgetpin-child
→ Widget
</dt>
<dd>
  The pinned Widget controlled by this /sdk-for-flutter-navigate-mapview-widgetpin-class.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="coordinates">
/sdk-for-flutter-navigate-mapview-widgetpin-coordinates
↔ /sdk-for-flutter-navigate-core-geocoordinates-class
</dt>
<dd>
  Gets geographical location of the /sdk-for-flutter-navigate-mapview-widgetpin-class.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-mapview-widgetpin-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapview-widgetpin-runtimetype
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
<dt class="callable" id="makeWidget">
/sdk-for-flutter-navigate-mapview-widgetpin-makewidget(<wbr/>BuildContext context)
    → Widget

</dt>
<dd>
  Creates a widget for this /sdk-for-flutter-navigate-mapview-widgetpin-class.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapview-widgetpin-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapview-widgetpin-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="unpin">
/sdk-for-flutter-navigate-mapview-widgetpin-unpin(<wbr/>)
    → dynamic

</dt>
<dd>
  Removes this /sdk-for-flutter-navigate-mapview-widgetpin-class from the map.
  

</dd>
<dt class="callable" id="updateScreenPosition">
/sdk-for-flutter-navigate-mapview-widgetpin-updatescreenposition(<wbr/>/sdk-for-flutter-navigate-core-point2d-class? screenPosition)
    → dynamic

</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-mapview-widgetpin-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">WidgetPin class</li>
</ol>
<h5>mapview library</h5>
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
