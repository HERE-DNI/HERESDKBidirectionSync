---
title: "Untitled"
slug: "sdk-for-flutter-navigate-location-locationissuelistener-locationissuelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationIssueListener.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-location-locationissuelistener-class</li>
<li class="self-crumb">LocationIssueListener factory constructor</li>
</ol>
<div class="self-name">LocationIssueListener</div>
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
<div class="main-content" data-above-sidebar="location/LocationIssueListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>LocationIssueListener constructor</h1></div>
<section class="multi-line-signature">
LocationIssueListener(<wbr/><ol class="parameter-list single-line"> <li>void onLocationIssueChangedLambda(<ol class="parameter-list single-line"> <li>List&lt;<wbr/>/sdk-for-flutter-navigate-location-locationissuetype&gt;</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>abstract class receiving notifications when the set of
currently active location issues changes.</p>
<p>Location issues represent unexpected or degraded conditions affecting positioning quality,
availability, or functionality. The LocationEngine monitors various positioning subsystems
and aggregates detected issues into a unified snapshot delivered via this interface.</p>
<ul>
<li>Each callback delivers the complete current set of active issues.</li>
<li>An empty list indicates all previously reported issues have cleared.</li>
<li>Issues are transient by design and automatically removed once underlying conditions improve.
No explicit clear/dismiss API is provided.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory LocationIssueListener(
  void Function(List&lt;LocationIssueType&gt;) onLocationIssueChangedLambda,

) =&gt; LocationIssueListener$Lambdas(
  onLocationIssueChangedLambda,

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
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-location-locationissuelistener-class</li>
<li class="self-crumb">LocationIssueListener factory constructor</li>
</ol>
<h5>LocationIssueListener class</h5>
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
