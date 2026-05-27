---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-lookatdistancewitheasing"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- lookAtDistanceWithEasing.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapCameraKeyframeTrack-class.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class</a></li>
<li class="self-crumb">lookAtDistanceWithEasing static method</li>
</ol>
<div class="self-name">lookAtDistanceWithEasing</div>
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
<div class="main-content" data-above-sidebar="mapview/MapCameraKeyframeTrack-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>lookAtDistanceWithEasing static method</h1></div>
<section class="multi-line-signature">
<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.27.0. Use [MapCameraKeyframeTrack.lookAtDistanceWithKind] instead.")</li>
</ol>
</div>
<a href="../../mapview/MapCameraKeyframeTrack-class.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class</a>
lookAtDistanceWithEasing(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/><a href="../../animation/ScalarKeyframe-class.html">/sdk-for-flutter-explore-animation-scalarkeyframe-class</a>&gt; keyframes, </li>
<li><a href="../../animation/Easing-class.html">/sdk-for-flutter-explore-animation-easing-class</a> easing, </li>
<li><a href="../../animation/KeyframeInterpolationMode.html">/sdk-for-flutter-explore-animation-keyframeinterpolationmode</a> interpolationMode</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates a map camera look-at distance keyframe track.</p>
<p>It enables animations of the distance
from the map camera to the target point that the camera looks at in meters. The values will
be clamped according to the minimum and maximum zoom levels set for the map camera.</p>
<ul>
<li>
<p><code>keyframes</code> The list of keyframes that specify how the camera property is changed.
Keyframe time offsets are considered to be relative to the previous keyframe
in the list or relative to the start of the animation if the current keyframe
is first in the list.
Time offset of the first keyframe in the list should be 0, otherwise an error occurs
and creation of the keyframe track will fail.</p>
</li>
<li>
<p><code>easing</code> The easing to apply during keyframe interpolation.</p>
</li>
<li>
<p><code>interpolationMode</code> The type of interpolation done between keyframe values.</p>
</li>
</ul>
<p>Returns <a href="../../mapview/MapCameraKeyframeTrack-class.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class</a>. A keyframe track over the distance from the map camera to its target.</p>
<p>Throws <a href="../../mapview/MapCameraKeyframeTrackInstantiationException-class.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrackinstantiationexception-class</a>. Indicates an instantiation issue.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.27.0. Use [MapCameraKeyframeTrack.lookAtDistanceWithKind] instead.")

static MapCameraKeyframeTrack lookAtDistanceWithEasing(List&lt;ScalarKeyframe&gt; keyframes, Easing easing, KeyframeInterpolationMode interpolationMode) =&gt; $prototype.lookAtDistanceWithEasing(keyframes, easing, interpolationMode);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapCameraKeyframeTrack-class.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class</a></li>
<li class="self-crumb">lookAtDistanceWithEasing static method</li>
</ol>
<h5>MapCameraKeyframeTrack class</h5>
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
