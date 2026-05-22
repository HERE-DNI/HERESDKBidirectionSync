---
title: "Untitled"
slug: "sdk-for-flutter-navigate-core-engine-logcontrol-setcustomappender"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setCustomAppender.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-navigate-core-engine-logcontrol-class</li>
<li class="self-crumb">setCustomAppender static method</li>
</ol>
<div class="self-name">setCustomAppender</div>
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
<div class="main-content" data-above-sidebar="core.engine/LogControl-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>setCustomAppender static method</h1></div>
<section class="multi-line-signature">
void
setCustomAppender(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-engine-loglevel level, </li>
<li>/sdk-for-flutter-navigate-core-engine-logappender-class appender</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Sets a custom log appender to receive log messages from the SDK.</p>
<p>This overwrites a previous custom log appender set by user.
Note, that setting the custom appender does not disable logging to the console made by SDK,
in order to do that use /sdk-for-flutter-navigate-core-engine-logcontrol-disableloggingtoconsole API.</p>
<ul>
<li>
<p><code>level</code> Log level.</p>
</li>
<li>
<p><code>appender</code> New log appender.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static void setCustomAppender(LogLevel level, LogAppender appender) =&gt; $prototype.setCustomAppender(level, appender);</code></pre>
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
<li>/sdk-for-flutter-navigate-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-navigate-core-engine-logcontrol-class</li>
<li class="self-crumb">setCustomAppender static method</li>
</ol>
<h5>LogControl class</h5>
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
