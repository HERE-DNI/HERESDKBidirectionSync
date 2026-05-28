---
title: "lookAtOrientationWithEasing static method"
slug: "sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-lookatorientationwitheasing"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtOrientationWithEasing.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class</li>
<li class="self-crumb">lookAtOrientationWithEasing static method</li>
</ol>
<div class="self-name">lookAtOrientationWithEasing</div>
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
<h1>lookAtOrientationWithEasing static method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class
lookAtOrientationWithEasing(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/>/sdk-for-flutter-navigate-animation-geoorientationkeyframe-class&gt; keyframes, </li>
<li>/sdk-for-flutter-navigate-animation-easing-class easing, </li>
<li>/sdk-for-flutter-navigate-animation-keyframeinterpolationmode interpolationMode</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates a map camera look-at orientation keyframe track.</p>
<p>It enables animations over the
orientation of the map camera target (bearing and tilt).</p>
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
<p>Returns /sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class. A keyframe track over the map camera target orientation.</p>
<p>Throws /sdk-for-flutter-navigate-mapview-mapcamerakeyframetrackinstantiationexception-class. Indicates an instantiation issue.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraKeyframeTrack lookAtOrientationWithEasing(List&lt;GeoOrientationKeyframe&gt; keyframes, Easing easing, KeyframeInterpolationMode interpolationMode) =&gt; $prototype.lookAtOrientationWithEasing(keyframes, easing, interpolationMode);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class</li>
<li class="self-crumb">lookAtOrientationWithEasing static method</li>
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
`
}</HTMLBlock>
