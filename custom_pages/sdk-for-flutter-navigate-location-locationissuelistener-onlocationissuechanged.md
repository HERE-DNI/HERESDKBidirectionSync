---
title: "onLocationIssueChanged abstract method"
slug: "sdk-for-flutter-navigate-location-locationissuelistener-onlocationissuechanged"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onLocationIssueChanged.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-location-locationissuelistener-class</li>
<li class="self-crumb">onLocationIssueChanged abstract method</li>
</ol>
<div class="self-name">onLocationIssueChanged</div>
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
<h1>onLocationIssueChanged abstract method</h1></div>
<section class="multi-line-signature">
void
onLocationIssueChanged(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/>/sdk-for-flutter-navigate-location-locationissuetype&gt; issues</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Called when the snapshot of currently active location issues changes.</p>
<p>Invoked whenever the LocationEngine detects a change in the set of active issues,
including when all issues clear (empty list). Replace any previously stored issue
list with this snapshot.</p>
<ul>
<li><code>issues</code> Current snapshot of active location issues. Empty list indicates no active issues.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onLocationIssueChanged(List&lt;LocationIssueType&gt; issues);</code></pre>
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
<li class="self-crumb">onLocationIssueChanged abstract method</li>
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
</div></div>
</div>
`
}</HTMLBlock>
