---
title: "cancel abstract method"
slug: "sdk-for-flutter-explore-core-threading-taskhandle-cancel"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- cancel.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-threading-core-threading-library</li>
<li>/sdk-for-flutter-explore-core-threading-taskhandle-class</li>
<li class="self-crumb">cancel abstract method</li>
</ol>
<div class="self-name">cancel</div>
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
<div class="main-content" data-above-sidebar="core.threading/TaskHandle-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>cancel abstract method</h1></div>
<section class="multi-line-signature">
bool
cancel(<wbr/>)

      

    </section>
<section class="desc markdown">
<p>Sets internal state of task to 'canceled'.</p>
<p>If the task is still in the queue, it will be
removed from it immediately. However, if the task is in a running state, it will nevertheless be completed, as there is no way
to interrupt it.</p>
<p>Returns <code>bool</code>. True, if the task was canceled.</p>
<p>False, if the task can't be canceled due to a
platform dependent reason.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool cancel();</code></pre>
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
<li>/sdk-for-flutter-explore-core-threading-core-threading-library</li>
<li>/sdk-for-flutter-explore-core-threading-taskhandle-class</li>
<li class="self-crumb">cancel abstract method</li>
</ol>
<h5>TaskHandle class</h5>
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
