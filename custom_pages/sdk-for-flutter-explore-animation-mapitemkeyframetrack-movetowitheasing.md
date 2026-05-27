---
title: "moveToWithEasing static method"
slug: "sdk-for-flutter-explore-animation-mapitemkeyframetrack-movetowitheasing"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- moveToWithEasing.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-animation-animation-library</li>
<li>/sdk-for-flutter-explore-animation-mapitemkeyframetrack-class</li>
<li class="self-crumb">moveToWithEasing static method</li>
</ol>
<div class="self-name">moveToWithEasing</div>
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
<h1>moveToWithEasing static method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-explore-animation-mapitemkeyframetrack-class
moveToWithEasing(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/>/sdk-for-flutter-explore-animation-geocoordinateskeyframe-class&gt; keyframes, </li>
<li>/sdk-for-flutter-explore-animation-easing-class easing, </li>
<li>/sdk-for-flutter-explore-animation-keyframeinterpolationmode interpolationMode</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates a map item position keyframe track.</p>
<p>It enables animations over the geographical
coordinates where the map item is positioned.</p>
<ul>
<li>
<p><code>keyframes</code> The list of keyframes that specify how the map item position changes over time.</p>
</li>
<li>
<p><code>easing</code> The easing to apply during keyframe interpolation.</p>
</li>
<li>
<p><code>interpolationMode</code> The type of interpolation done between keyframe values.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-explore-animation-mapitemkeyframetrack-class. MapItemKeyFrameTrack instance.</p>
<p>Throws /sdk-for-flutter-explore-animation-mapitemkeyframetrackinstantiationexception-class. If the supplied keyframe list is empty or first keyframe duration is not 0.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapItemKeyFrameTrack moveToWithEasing(List&lt;GeoCoordinatesKeyframe&gt; keyframes, Easing easing, KeyframeInterpolationMode interpolationMode) =&gt; $prototype.moveToWithEasing(keyframes, easing, interpolationMode);</code></pre>
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
<li>/sdk-for-flutter-explore-animation-mapitemkeyframetrack-class</li>
<li class="self-crumb">moveToWithEasing static method</li>
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
`
}</HTMLBlock>
