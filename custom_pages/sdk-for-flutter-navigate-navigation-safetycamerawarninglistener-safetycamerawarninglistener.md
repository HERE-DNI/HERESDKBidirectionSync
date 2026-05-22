---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-safetycamerawarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SafetyCameraWarningListener.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class</li>
<li class="self-crumb">SafetyCameraWarningListener factory constructor</li>
</ol>
<div class="self-name">SafetyCameraWarningListener</div>
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
<div class="main-content" data-above-sidebar="navigation/SafetyCameraWarningListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>SafetyCameraWarningListener constructor</h1></div>
<section class="multi-line-signature">
SafetyCameraWarningListener(<wbr/><ol class="parameter-list single-line"> <li>void onSafetyCameraWarningUpdatedLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-safetycamerawarning-class</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>This abstract class
should be implemented in order to receive notifications on safety cameras.</p>
<p>A <code>SafetyCameraWarning</code> will not be given until the previous warning of that type has been passed.
For example, a route with <code>SafetyCameraWarning</code> 120 meters and <code>SafetyCameraWarning</code> 160 meters ahead,
the first <code>SafetyCameraWarning.distance_to_camera_in_meters</code> is 120 meters
and the next <code>SafetyCameraWarning.distance_to_camera_in_meters</code> is then 40 meters,
since that is the distance between the first and second warnings.</p>
<p>When <code>SafetyCameraWarningListener</code> is enabled, a new set of text notifications (e.g. "Speed camera ahead") will be trigger if any has been also enabled.
The updates for the same safety camera appear in order of the initial <code>DistanceType.AHEAD</code> event.
That is a first in first out approach is used when multiple safety cameras are reached or passed on the same location.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory SafetyCameraWarningListener(
  void Function(SafetyCameraWarning) onSafetyCameraWarningUpdatedLambda,

) =&gt; SafetyCameraWarningListener$Lambdas(
  onSafetyCameraWarningUpdatedLambda,

);</code></pre>
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
<li>/sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class</li>
<li class="self-crumb">SafetyCameraWarningListener factory constructor</li>
</ol>
<h5>SafetyCameraWarningListener class</h5>
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
