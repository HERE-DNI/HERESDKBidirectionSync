---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-normalizedprincipalpointwitheasing"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- normalizedPrincipalPointWithEasing.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapCameraKeyframeTrack-class.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class</a></li>
<li class="self-crumb">normalizedPrincipalPointWithEasing static method</li>
</ol>
<div class="self-name">normalizedPrincipalPointWithEasing</div>
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
<h1>normalizedPrincipalPointWithEasing static method</h1></div>
<section class="multi-line-signature">
<a href="../../mapview/MapCameraKeyframeTrack-class.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class</a>
normalizedPrincipalPointWithEasing(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/><a href="../../animation/Anchor2DKeyframe-class.html">/sdk-for-flutter-explore-animation-anchor2dkeyframe-class</a>&gt; keyframes, </li>
<li><a href="../../animation/Easing-class.html">/sdk-for-flutter-explore-animation-easing-class</a> easing, </li>
<li><a href="../../animation/KeyframeInterpolationMode.html">/sdk-for-flutter-explore-animation-keyframeinterpolationmode</a> interpolationMode</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates a map camera principal point keyframe track.</p>
<p>It enables animations on the point
where the map camera's target is placed in normalized view coordinates. (0,0) is top left of
the viewport, (1, 1) is bottom right.</p>
<ul>
<li>
<p><code>keyframes</code> The list of keyframes that specify how the camera property is changed.
Point values must be in normalized screen coordinates with origin (0,0) in the top left and (1,1) in the bottom right of the viewport.
Point values outside of viewport boundaries will be clamped to the viewport boundaries during animation.
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
<p>Returns <a href="../../mapview/MapCameraKeyframeTrack-class.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class</a>. A keyframe track over the principal point.</p>
<p>Throws <a href="../../mapview/MapCameraKeyframeTrackInstantiationException-class.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrackinstantiationexception-class</a>. Indicates an instantiation issue.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraKeyframeTrack normalizedPrincipalPointWithEasing(List&lt;Anchor2DKeyframe&gt; keyframes, Easing easing, KeyframeInterpolationMode interpolationMode) =&gt; $prototype.normalizedPrincipalPointWithEasing(keyframes, easing, interpolationMode);</code></pre>
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
<li class="self-crumb">normalizedPrincipalPointWithEasing static method</li>
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
