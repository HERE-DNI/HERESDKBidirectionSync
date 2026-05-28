---
title: "LogAppender constructor"
slug: "sdk-for-flutter-explore-core-engine-logappender-logappender"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LogAppender.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-explore-core-engine-logappender-class</li>
<li class="self-crumb">LogAppender factory constructor</li>
</ol>
<div class="self-name">LogAppender</div>
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
<div class="main-content" data-above-sidebar="core.engine/LogAppender-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>LogAppender constructor</h1></div>
<section class="multi-line-signature">
LogAppender(<wbr/><ol class="parameter-list single-line"> <li>void logLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-core-engine-loglevel, </li>
<li>String</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>An interface to implement a listener to receive log messages.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory LogAppender(
  void Function(LogLevel, String) logLambda,

) =&gt; LogAppender$Lambdas(
  logLambda,

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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-explore-core-engine-logappender-class</li>
<li class="self-crumb">LogAppender factory constructor</li>
</ol>
<h5>LogAppender class</h5>
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
