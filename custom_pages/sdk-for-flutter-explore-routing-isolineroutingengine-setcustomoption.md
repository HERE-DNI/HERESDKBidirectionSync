---
title: "setCustomOption abstract method"
slug: "sdk-for-flutter-explore-routing-isolineroutingengine-setcustomoption"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setCustomOption.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-routing-isolineroutingengine-class</li>
<li class="self-crumb">setCustomOption abstract method</li>
</ol>
<div class="self-name">setCustomOption</div>
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
<div class="main-content" data-above-sidebar="routing/IsolineRoutingEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>setCustomOption abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-explore-routing-routingerror?
setCustomOption(<wbr/><ol class="parameter-list single-line"> <li>String name, </li>
<li>String? value</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Sets a custom option for routing backend queries.</p>
<p>The custom option is applied to all the queries that <code>IsolineRoutingEngine</code> performs.
For a complete list of available parameter names and their valid values, refer to
<a href="https://www.here.com/docs/bundle/batch-api-developer-guide/page/topics/constructing-request.html">HERE Routing API v8</a>.
<strong>Note:</strong> It's easy to set a wrong option that makes queries invalid,
so make sure you read and understand the backend documentation.</p>
<ul>
<li>
<p><code>name</code> An option name. If the engine already has an option with the same name, the option will be overwritten. The option name must be a non-empty string.
The option name should't duplicate option names that SDK creates by itself for usage in the query,
otherwise the query will callback with the error <code>RoutingError.INTERNAL_ERROR</code>.</p>
</li>
<li>
<p><code>value</code> An option value. If the value is <code>null</code>, the option will be removed. The option value must be a non-empty string.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-explore-routing-routingerror. An optional error of setting the option.</p>
<p>It's <code>null</code> if the option has been set successfully.
It's <code>RoutingError.INVALID_PARAMETER</code> if the input name and/or value haven't passed internal validation.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">RoutingError? setCustomOption(String name, String? value);</code></pre>
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
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-routing-isolineroutingengine-class</li>
<li class="self-crumb">setCustomOption abstract method</li>
</ol>
<h5>IsolineRoutingEngine class</h5>
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
