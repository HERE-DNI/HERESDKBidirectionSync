---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mapcameraanimationfactory-createanimationfromkeyframetracks"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- createAnimationFromKeyframeTracks.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapCameraAnimationFactory-class.html">/sdk-for-flutter-explore-mapview-mapcameraanimationfactory-class</a></li>
<li class="self-crumb">createAnimationFromKeyframeTracks static method</li>
</ol>
<div class="self-name">createAnimationFromKeyframeTracks</div>
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
<div class="main-content" data-above-sidebar="mapview/MapCameraAnimationFactory-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>createAnimationFromKeyframeTracks static method</h1></div>
<section class="multi-line-signature">
<a href="../../mapview/MapCameraAnimation-class.html">/sdk-for-flutter-explore-mapview-mapcameraanimation-class</a>
createAnimationFromKeyframeTracks(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/><a href="../../mapview/MapCameraKeyframeTrack-class.html">/sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class</a>&gt; tracks</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates a MapCameraAnimation for a movement defined by the supplied list of <code>MapCameraAnimationFactory.createAnimationFromKeyframeTracks.tracks</code>.</p>
<p>Keyframe tracks specify how the map camera properties change during the animation.
For the animation to be possible, no two different tracks can
affect the same map camera property. The input tracks are validated with that in mind.</p>
<p>However, the following cases can only be detected at the time when animation is started:</p>
<ul>
<li>
<p>Changing altitude of camera position also changes camera look-at distance
and at high altitudes, also camera look-at orientation.</p>
</li>
<li>
<p>Changing tilt of camera orientation also changes camera look-at distance
and camera look-at target.</p>
</li>
<li>
<p>Changing bearing of camera orientation also changes
camera look-at target if current tilt is not 0.</p>
</li>
<li>
<p>Changing tilt or bearing of camera look-at orientation also changes
camera position.</p>
</li>
<li>
<p>Changing camera look-at orientation also changes camera look-at distance
if tilt is not 0.</p>
</li>
<li>
<p><code>tracks</code> The list of tracks</p>
</li>
</ul>
<p>Returns <a href="../../mapview/MapCameraAnimation-class.html">/sdk-for-flutter-explore-mapview-mapcameraanimation-class</a>. MapCameraAnimation instance</p>
<p>Throws <a href="../../mapview/MapCameraAnimationInstantiationException-class.html">/sdk-for-flutter-explore-mapview-mapcameraanimationinstantiationexception-class</a>. Indicates an instantiation issue.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraAnimation createAnimationFromKeyframeTracks(List&lt;MapCameraKeyframeTrack&gt; tracks) =&gt; $prototype.createAnimationFromKeyframeTracks(tracks);</code></pre>
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
<li><a href="../../mapview/MapCameraAnimationFactory-class.html">/sdk-for-flutter-explore-mapview-mapcameraanimationfactory-class</a></li>
<li class="self-crumb">createAnimationFromKeyframeTracks static method</li>
</ol>
<h5>MapCameraAnimationFactory class</h5>
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
