---
title: "Implementation"
slug: "sdk-for-flutter-explore-animation-mapitemkeyframetrack-polylineprogresswitheasing"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- polylineProgressWithEasing.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../animation/animation-library.html">/sdk-for-flutter-explore-animation-animation-library</a></li>
<li><a href="../../animation/MapItemKeyFrameTrack-class.html">/sdk-for-flutter-explore-animation-mapitemkeyframetrack-class</a></li>
<li class="self-crumb">polylineProgressWithEasing static method</li>
</ol>
<div class="self-name">polylineProgressWithEasing</div>
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
<div class="main-content" data-above-sidebar="animation/MapItemKeyFrameTrack-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>polylineProgressWithEasing static method</h1></div>
<section class="multi-line-signature">
<a href="../../animation/MapItemKeyFrameTrack-class.html">/sdk-for-flutter-explore-animation-mapitemkeyframetrack-class</a>
polylineProgressWithEasing(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/><a href="../../animation/ScalarKeyframe-class.html">/sdk-for-flutter-explore-animation-scalarkeyframe-class</a>&gt; keyframes, </li>
<li><a href="../../animation/Easing-class.html">/sdk-for-flutter-explore-animation-easing-class</a> easing, </li>
<li><a href="../../animation/KeyframeInterpolationMode.html">/sdk-for-flutter-explore-animation-keyframeinterpolationmode</a> interpolationMode</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates a keyframe track used to animate the progress of a polyline.</p>
<p>Each scalar keyframe specifies the value of <a href="../../mapview/MapPolyline/progress.html">/sdk-for-flutter-explore-mapview-mappolyline-progress</a>
at key points of the animation.</p>
<ul>
<li>
<p><code>keyframes</code> The list of keyframes that specify how the polyline progress changes
over time.</p>
</li>
<li>
<p><code>easing</code> The easing to apply during keyframe interpolation.</p>
</li>
<li>
<p><code>interpolationMode</code> The type of interpolation done between keyframe values.</p>
</li>
</ul>
<p>Returns <a href="../../animation/MapItemKeyFrameTrack-class.html">/sdk-for-flutter-explore-animation-mapitemkeyframetrack-class</a>. MapItemKeyFrameTrack instance.</p>
<p>Throws <a href="../../animation/MapItemKeyFrameTrackInstantiationException-class.html">/sdk-for-flutter-explore-animation-mapitemkeyframetrackinstantiationexception-class</a>. If the supplied keyframe list is empty or first keyframe duration is not 0.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapItemKeyFrameTrack polylineProgressWithEasing(List&lt;ScalarKeyframe&gt; keyframes, Easing easing, KeyframeInterpolationMode interpolationMode) =&gt; $prototype.polylineProgressWithEasing(keyframes, easing, interpolationMode);</code></pre>
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
<li><a href="../../animation/animation-library.html">/sdk-for-flutter-explore-animation-animation-library</a></li>
<li><a href="../../animation/MapItemKeyFrameTrack-class.html">/sdk-for-flutter-explore-animation-mapitemkeyframetrack-class</a></li>
<li class="self-crumb">polylineProgressWithEasing static method</li>
</ol>
<h5>MapItemKeyFrameTrack class</h5>
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
