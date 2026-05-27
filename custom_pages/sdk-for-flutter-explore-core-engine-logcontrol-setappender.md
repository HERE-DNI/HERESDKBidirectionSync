---
title: "Implementation"
slug: "sdk-for-flutter-explore-core-engine-logcontrol-setappender"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- setAppender.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li><a href="../../core.engine/LogControl-class.html">/sdk-for-flutter-explore-core-engine-logcontrol-class</a></li>
<li class="self-crumb">setAppender static method</li>
</ol>
<div class="self-name">setAppender</div>
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
<h1>setAppender static method</h1></div>
<section class="multi-line-signature">
void
setAppender(<wbr/><ol class="parameter-list single-line"> <li><a href="../../core.engine/LogLevel.html">/sdk-for-flutter-explore-core-engine-loglevel</a> level, </li>
<li>String path</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Sets a custom log appender that will write SDK log messages to a file.</p>
<p>This overwrites a previous custom log appender set by user.
Note, that setting the custom appender does not disable logging to the console made by SDK,
in order to do that use <a href="../../core.engine/LogControl/disableLoggingToConsole.html">/sdk-for-flutter-explore-core-engine-logcontrol-disableloggingtoconsole</a> API.</p>
<ul>
<li>
<p><code>level</code> Log level.</p>
</li>
<li>
<p><code>path</code> Absolute path to a file that the application has read/write permissions.</p>
</li>
</ul>
<p>Throws <a href="../../core.engine/LogControlInvalidPathExceptionException-class.html">/sdk-for-flutter-explore-core-engine-logcontrolinvalidpathexceptionexception-class</a>. <a href="../../core.engine/LogControlInvalidPathExceptionException-class.html">/sdk-for-flutter-explore-core-engine-logcontrolinvalidpathexceptionexception-class</a> Indicates that the file path is invalid or not writeable.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static void setAppender(LogLevel level, String path) =&gt; $prototype.setAppender(level, path);</code></pre>
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
<li><a href="../../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li><a href="../../core.engine/LogControl-class.html">/sdk-for-flutter-explore-core-engine-logcontrol-class</a></li>
<li class="self-crumb">setAppender static method</li>
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
</div></div>
</div>
</HTMLBlock>
