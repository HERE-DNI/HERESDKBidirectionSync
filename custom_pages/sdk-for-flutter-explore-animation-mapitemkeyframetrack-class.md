---
title: "MapItemKeyFrameTrack class abstract"
slug: "sdk-for-flutter-explore-animation-mapitemkeyframetrack-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapItemKeyFrameTrack-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="animation/MapItemKeyFrameTrack-class.html#constructors">Constructors</a></li>
<li><a href="animation/MapItemKeyFrameTrack/MapItemKeyFrameTrack.html">MapItemKeyFrameTrack</a></li>
<li class="section-title inherited">
<a href="animation/MapItemKeyFrameTrack-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="animation/MapItemKeyFrameTrack/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="animation/MapItemKeyFrameTrack/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="animation/MapItemKeyFrameTrack-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="animation/MapItemKeyFrameTrack/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="animation/MapItemKeyFrameTrack/toString.html">toString</a></li>
<li class="section-title inherited"><a href="animation/MapItemKeyFrameTrack-class.html#operators">Operators</a></li>
<li class="inherited"><a href="animation/MapItemKeyFrameTrack/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="animation/MapItemKeyFrameTrack-class.html#static-methods">Static methods</a></li>
<li><a href="animation/MapItemKeyFrameTrack/moveToWithEasing.html">moveToWithEasing</a></li>
<li><a href="animation/MapItemKeyFrameTrack/polylineProgressWithEasing.html">polylineProgressWithEasing</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-animation-animation-library</li>
<li class="self-crumb">MapItemKeyFrameTrack class</li>
</ol>
<div class="self-name">MapItemKeyFrameTrack</div>
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
<div class="main-content" data-above-sidebar="animation/animation-library-sidebar.html" data-below-sidebar="animation/MapItemKeyFrameTrack-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapItemKeyFrameTrack class abstract</h1></div>
<section class="desc markdown">
<p>Stores keyframes for interpolation of a map item property using a specific
easing function and interpolation mode.</p>
<p>The keyframe track object is used to create animations,
see /sdk-for-flutter-explore-animation-mapmarkeranimation-class and /sdk-for-flutter-explore-animation-mappolylineanimation-class.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapItemKeyFrameTrack">
/sdk-for-flutter-explore-animation-mapitemkeyframetrack-mapitemkeyframetrack()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-animation-mapitemkeyframetrack-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-animation-mapitemkeyframetrack-runtimetype
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
/sdk-for-flutter-explore-animation-mapitemkeyframetrack-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-animation-mapitemkeyframetrack-tostring(<wbr/>)
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
/sdk-for-flutter-explore-animation-mapitemkeyframetrack-operator-equals(<wbr/>Object other)
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
<dt class="callable" id="moveToWithEasing">
/sdk-for-flutter-explore-animation-mapitemkeyframetrack-movetowitheasing(<wbr/>List&lt;<wbr/>/sdk-for-flutter-explore-animation-geocoordinateskeyframe-class&gt; keyframes, /sdk-for-flutter-explore-animation-easing-class easing, /sdk-for-flutter-explore-animation-keyframeinterpolationmode interpolationMode)
    → /sdk-for-flutter-explore-animation-mapitemkeyframetrack-class

</dt>
<dd>
  Creates a map item position keyframe track.
  

</dd>
<dt class="callable" id="polylineProgressWithEasing">
/sdk-for-flutter-explore-animation-mapitemkeyframetrack-polylineprogresswitheasing(<wbr/>List&lt;<wbr/>/sdk-for-flutter-explore-animation-scalarkeyframe-class&gt; keyframes, /sdk-for-flutter-explore-animation-easing-class easing, /sdk-for-flutter-explore-animation-keyframeinterpolationmode interpolationMode)
    → /sdk-for-flutter-explore-animation-mapitemkeyframetrack-class

</dt>
<dd>
  Creates a keyframe track used to animate the progress of a polyline.
  

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
<li>/sdk-for-flutter-explore-animation-animation-library</li>
<li class="self-crumb">MapItemKeyFrameTrack class</li>
</ol>
<h5>animation library</h5>
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
