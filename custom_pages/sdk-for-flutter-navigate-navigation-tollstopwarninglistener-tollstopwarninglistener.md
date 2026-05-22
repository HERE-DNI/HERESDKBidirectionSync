---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-tollstopwarninglistener-tollstopwarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TollStopWarningListener.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-tollstopwarninglistener-class</li>
<li class="self-crumb">TollStopWarningListener factory constructor</li>
</ol>
<div class="self-name">TollStopWarningListener</div>
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
<div class="main-content" data-above-sidebar="navigation/TollStopWarningListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>TollStopWarningListener constructor</h1></div>
<section class="multi-line-signature">
TollStopWarningListener(<wbr/><ol class="parameter-list single-line"> <li>void onTollStopWarningLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-tollstop-class</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>This abstract class
should be implemented in order to receive information on the upcoming toll booth structure.</p>
<p>The warner might also warn about gates/checkpoints for vignette, border checkpoints
and similar structures on the street.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.
A <code>TollStop</code> will not be given until the previous warning of that type has been passed.
For example, a route with <code>TollStop</code> 120 meters and <code>TollStop</code> 160 meters ahead,
the first <code>TollStop.distance_to_toll_stop_in_meters</code> is 120 meters
and the next <code>TollStop.distance_to_toll_stop_in_meters</code> is then 40 meters,
since that is the distance between the first and second warnings.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory TollStopWarningListener(
  void Function(TollStop) onTollStopWarningLambda,

) =&gt; TollStopWarningListener$Lambdas(
  onTollStopWarningLambda,

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
<li>/sdk-for-flutter-navigate-navigation-tollstopwarninglistener-class</li>
<li class="self-crumb">TollStopWarningListener factory constructor</li>
</ol>
<h5>TollStopWarningListener class</h5>
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
