---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-spatialaudiocuepanning-startangularpanning"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startAngularPanning.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-spatialaudiocuepanning-class</li>
<li class="self-crumb">startAngularPanning abstract method</li>
</ol>
<div class="self-name">startAngularPanning</div>
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
<div class="main-content" data-above-sidebar="navigation/SpatialAudioCuePanning-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>startAngularPanning abstract method</h1></div>
<section class="multi-line-signature">
void
startAngularPanning(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-custompanningdata-class? nextCustomPanningData, </li>
<li>/sdk-for-flutter-navigate-navigation-spatialaudiocuepanningspatialazimuthstarted azimuthCallback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>This method will retrieve a stream of azimuth values to be passed onto the spatial audio renderer.</p>
<p>An optional custom value for /sdk-for-flutter-navigate-navigation-custompanningdata-estimatedaudiocueduration,
/sdk-for-flutter-navigate-navigation-custompanningdata-initialazimuthindegrees,  or its /sdk-for-flutter-navigate-navigation-custompanningdata-sweepazimuthindegrees
can be here defined if the default data does not fully match the utilized Language or TTS engine
or angle expectations.
If startAngularPanning is called to spatialize the audio cue of a new maneuver before the full
completion of a previous spatial audio trajectory, then /sdk-for-flutter-navigate-navigation-eventtextlistener-class will retrieve
the azimuth values of the new maneuver.</p>
<ul>
<li>
<p><code>nextCustomPanningData</code> Defines a new set of values related to spatial audio panning.
When /sdk-for-flutter-navigate-navigation-custompanningdata-class is initialized as <code>null</code>, the default set of values provided by HERE SDK
will be used instead.</p>
</li>
<li>
<p><code>azimuthCallback</code> Callback that will signal the next azimuth required to complete a spatial audio trajectory
once the angular panning has started.
Azimuth angular values are retrieved individually until the full duration of the audio trajectory
has been reached,
or a new text message has started its angular panning.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void startAngularPanning(CustomPanningData? nextCustomPanningData, SpatialAudioCuePanningspatialAzimuthStarted azimuthCallback);</code></pre>
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
<li>/sdk-for-flutter-navigate-navigation-spatialaudiocuepanning-class</li>
<li class="self-crumb">startAngularPanning abstract method</li>
</ol>
<h5>SpatialAudioCuePanning class</h5>
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
