---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-mapcameraanimationfactory-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapCameraAnimationFactory-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">MapCameraAnimationFactory class</li>
</ol>
<div class="self-name">MapCameraAnimationFactory</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapCameraAnimationFactory-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapCameraAnimationFactory class abstract</h1></div>
<section class="desc markdown">
<p>Factory for creating MapCameraAnimation objects to change map's camera over time.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapCameraAnimationFactory">
/sdk-for-flutter-explore-mapview-mapcameraanimationfactory-mapcameraanimationfactory()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-mapview-mapcameraanimationfactory-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-mapview-mapcameraanimationfactory-runtimetype
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
/sdk-for-flutter-explore-mapview-mapcameraanimationfactory-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-mapview-mapcameraanimationfactory-tostring(<wbr/>)
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
/sdk-for-flutter-explore-mapview-mapcameraanimationfactory-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-methods">
<h2>Static Methods</h2>
<dl class="callables">
<dt class="callable" id="createAnimationFromKeyframeTrack">
/sdk-for-flutter-explore-mapview-mapcameraanimationfactory-createanimationfromkeyframetrack(<wbr/>/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class track)
    → /sdk-for-flutter-explore-mapview-mapcameraanimation-class

</dt>
<dd>
  Creates a MapCameraAnimation for a movement defined by the supplied <code>MapCameraAnimationFactory.createAnimationFromKeyframeTrack.track</code>.
  

</dd>
<dt class="callable" id="createAnimationFromKeyframeTracks">
/sdk-for-flutter-explore-mapview-mapcameraanimationfactory-createanimationfromkeyframetracks(<wbr/>List&lt;<wbr/>/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class&gt; tracks)
    → /sdk-for-flutter-explore-mapview-mapcameraanimation-class

</dt>
<dd>
  Creates a MapCameraAnimation for a movement defined by the supplied list of <code>MapCameraAnimationFactory.createAnimationFromKeyframeTracks.tracks</code>.
  

</dd>
<dt class="callable" id="createAnimationFromUpdateWithEasing">
/sdk-for-flutter-explore-mapview-mapcameraanimationfactory-createanimationfromupdatewitheasing(<wbr/>/sdk-for-flutter-explore-mapview-mapcameraupdate-class cameraUpdate, Duration duration, /sdk-for-flutter-explore-animation-easing-class easing)
    → /sdk-for-flutter-explore-mapview-mapcameraanimation-class

</dt>
<dd>
  Creates a /sdk-for-flutter-explore-mapview-mapcameraanimation-class to gradually update the camera properties within a specified
duration from its current values to the ones defined in the <code>MapCameraAnimationFactory.createAnimationFromUpdateWithEasing.cameraUpdate</code>.
  

</dd>
<dt class="callable" id="flyTo">
/sdk-for-flutter-explore-mapview-mapcameraanimationfactory-flyto(<wbr/>/sdk-for-flutter-explore-core-geocoordinatesupdate-class target, double bowFactor, Duration duration)
    → /sdk-for-flutter-explore-mapview-mapcameraanimation-class

</dt>
<dd>
  Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve.
  

</dd>
<dt class="callable" id="flyToWithOrientation">
/sdk-for-flutter-explore-mapview-mapcameraanimationfactory-flytowithorientation(<wbr/>/sdk-for-flutter-explore-core-geocoordinatesupdate-class target, /sdk-for-flutter-explore-core-geoorientationupdate-class orientation, double bowFactor, Duration duration)
    → /sdk-for-flutter-explore-mapview-mapcameraanimation-class

</dt>
<dd>
  Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.
  

</dd>
<dt class="callable" id="flyToWithOrientationAndZoom">
/sdk-for-flutter-explore-mapview-mapcameraanimationfactory-flytowithorientationandzoom(<wbr/>/sdk-for-flutter-explore-core-geocoordinatesupdate-class target, /sdk-for-flutter-explore-core-geoorientationupdate-class orientation, /sdk-for-flutter-explore-mapview-mapmeasure-class zoom, double bowFactor, Duration duration)
    → /sdk-for-flutter-explore-mapview-mapcameraanimation-class

</dt>
<dd>
  Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.
  

</dd>
<dt class="callable" id="flyToWithZoom">
/sdk-for-flutter-explore-mapview-mapcameraanimationfactory-flytowithzoom(<wbr/>/sdk-for-flutter-explore-core-geocoordinatesupdate-class target, /sdk-for-flutter-explore-mapview-mapmeasure-class zoom, double bowFactor, Duration duration)
    → /sdk-for-flutter-explore-mapview-mapcameraanimation-class

</dt>
<dd>
  Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve.
  

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
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">MapCameraAnimationFactory class</li>
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
