---
title: "AreaCameraBehavior class abstract"
slug: "sdk-for-flutter-navigate-navigation-areacamerabehavior-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- AreaCameraBehavior-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/AreaCameraBehavior-class.html#constructors">Constructors</a></li>
<li><a href="navigation/AreaCameraBehavior/AreaCameraBehavior.html">AreaCameraBehavior</a></li>
<li class="section-title">
<a href="navigation/AreaCameraBehavior-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/AreaCameraBehavior/cameraAnimationDuration.html">cameraAnimationDuration</a></li>
<li><a href="navigation/AreaCameraBehavior/cameraBearingInDegrees.html">cameraBearingInDegrees</a></li>
<li><a href="navigation/AreaCameraBehavior/cameraTiltInDegrees.html">cameraTiltInDegrees</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/hashCode.html">hashCode</a></li>
<li><a href="navigation/AreaCameraBehavior/isCurrentPositionIncluded.html">isCurrentPositionIncluded</a></li>
<li><a href="navigation/AreaCameraBehavior/maxZoom.html">maxZoom</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/normalizedPrincipalPoint.html">normalizedPrincipalPoint</a></li>
<li><a href="navigation/AreaCameraBehavior/principalPointAnimationDuration.html">principalPointAnimationDuration</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/AreaCameraBehavior/viewRectangle.html">viewRectangle</a></li>
<li class="section-title"><a href="navigation/AreaCameraBehavior-class.html#instance-methods">Methods</a></li>
<li><a href="navigation/AreaCameraBehavior/getVisiblePoints.html">getVisiblePoints</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="navigation/AreaCameraBehavior/setVisiblePoints.html">setVisiblePoints</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/toString.html">toString</a></li>
<li class="section-title inherited"><a href="navigation/AreaCameraBehavior-class.html#operators">Operators</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">AreaCameraBehavior class</li>
</ol>
<div class="self-name">AreaCameraBehavior</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/AreaCameraBehavior-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>AreaCameraBehavior class abstract</h1></div>
<section class="desc markdown">
<p>Use this class to show an overview of geo points.</p>
<p>By default, the orientation of the camera will be
perpendicular to the Earth's surface (ie. looking towards the center of the Earth),
while bearing will be towards north.</p>
<p>Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API's are
subject to change without a deprecation process.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implemented types</dt>
<dd>
<ul class="comma-separated clazz-relationships">
<li>/sdk-for-flutter-navigate-navigation-camerabehavior-class</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="AreaCameraBehavior">
/sdk-for-flutter-navigate-navigation-areacamerabehavior-areacamerabehavior()
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
<dt class="property" id="cameraAnimationDuration">
/sdk-for-flutter-navigate-navigation-areacamerabehavior-cameraanimationduration
↔ Duration
</dt>
<dd>
  The duration of camera animation in milliseconds.
If there is an animation, it will last for specified period of time.
Defaults to 500 milliseconds, or half a second.
Gets the current animation duration in milliseconds.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="cameraBearingInDegrees">
/sdk-for-flutter-navigate-navigation-areacamerabehavior-camerabearingindegrees
↔ double
</dt>
<dd>
  Camera bearing in degrees.
The direction in which the camera will point in degrees clockwise, relative to
true North. The input should range between [0, 360]. Defaults to true North (0 degrees).
Gets the current camera bearing.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="cameraTiltInDegrees">
/sdk-for-flutter-navigate-navigation-areacamerabehavior-cameratiltindegrees
↔ double
</dt>
<dd>
  Camera tilt in degrees.
The tilt of the camera relative to the axis perpendicular to the ground. Defaults to
0 degrees, meaning that it will look straight down into the ground.
Gets the current camera tilt.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-navigation-camerabehavior-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="isCurrentPositionIncluded">
/sdk-for-flutter-navigate-navigation-areacamerabehavior-iscurrentpositionincluded
↔ bool
</dt>
<dd>
  Include current position in camera view.
Decides if the current position should be added to the set of visible points.
Note that if the current position is in the vicinity of any of the visible points, setting this to
<code>false</code> will not explicitly exclude the current position from the camera view. However if displaying
an area potentially away from the current position, this does need to be explicitly set to <code>false</code>
or it will try to include the current position. Defaults to false.
Gets whether to include the current position.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxZoom">
/sdk-for-flutter-navigate-navigation-areacamerabehavior-maxzoom
↔ /sdk-for-flutter-navigate-mapview-mapmeasure-class
</dt>
<dd>
  Maximal allowed zoom.
Defines maximal zoom level to be applied to enclose geodetic bounding box.
Defaults to a /sdk-for-flutter-navigate-mapview-mapmeasure-class with kind /sdk-for-flutter-navigate-mapview-mapmeasurekind and value 20.0.
Note: /sdk-for-flutter-navigate-mapview-mapmeasurekind is not supported.
Gets maximal allowed zoom.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="normalizedPrincipalPoint">
/sdk-for-flutter-navigate-navigation-camerabehavior-normalizedprincipalpoint
↔ /sdk-for-flutter-navigate-core-anchor2d-class
</dt>
<dd class="inherited">
  The normalized principal point.
Normalized principal point to be used during navigation.
Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom
of the mapview.
Gets the currently set normalized principal point to be used during navigation.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property" id="principalPointAnimationDuration">
/sdk-for-flutter-navigate-navigation-areacamerabehavior-principalpointanimationduration
↔ Duration
</dt>
<dd>
  The duration of principal point animation in milliseconds.
If the principal point is changed, the change will be animated
over this duration.
Defaults to 500 milliseconds, or half a second.
Gets the current principal point animation duration in milliseconds.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-camerabehavior-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="viewRectangle">
/sdk-for-flutter-navigate-navigation-areacamerabehavior-viewrectangle
↔ /sdk-for-flutter-navigate-core-rectangle2d-class?
</dt>
<dd>
  The view rectangle for camera updates.
Defines a sub-space of the screen that the behavior should consider
for camera updates.
Defaults to <code>null</code>. If not set, it uses the viewport bounds of the underlying map view.
Gets the current view rectangle, if it's set.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="getVisiblePoints">
/sdk-for-flutter-navigate-navigation-areacamerabehavior-getvisiblepoints(<wbr/>)
    → List&lt;<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class&gt;

</dt>
<dd>
  Gets configured visible geo points.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-camerabehavior-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="setVisiblePoints">
/sdk-for-flutter-navigate-navigation-areacamerabehavior-setvisiblepoints(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class&gt; visiblePoints)
    → void

</dt>
<dd>
  Sets the list of geo points to show in the camera view.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-camerabehavior-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-camerabehavior-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">AreaCameraBehavior class</li>
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
</div></div>
</div>
`
}</HTMLBlock>
