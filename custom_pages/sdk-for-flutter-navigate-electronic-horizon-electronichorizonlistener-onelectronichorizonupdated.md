---
title: "Untitled"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-onelectronichorizonupdated"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onElectronicHorizonUpdated.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-class</li>
<li class="self-crumb">onElectronicHorizonUpdated abstract method</li>
</ol>
<div class="self-name">onElectronicHorizonUpdated</div>
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
<div class="main-content" data-above-sidebar="electronic_horizon/ElectronicHorizonListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>onElectronicHorizonUpdated abstract method</h1></div>
<section class="multi-line-signature">
void
onElectronicHorizonUpdated(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonerrorcode? errorCode, </li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonupdate-class? update</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Called whenever the electronic horizon subsystem produces:</p>
<ul>
<li>a new update,</li>
<li>an error,</li>
</ul>
<p>The client must inspect <code>error_code</code> to determine whether the call
represents an error or a valid update.</p>
<ul>
<li>
<p><code>errorCode</code> The error associated with the horizon computation.
<code>null</code> means no error.</p>
</li>
<li>
<p><code>update</code> The update describing the current electronic horizon state.
May be <code>null</code> if an update could not be produced.</p>
</li>
</ul>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onElectronicHorizonUpdated(ElectronicHorizonErrorCode? errorCode, ElectronicHorizonUpdate? update);</code></pre>
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
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-class</li>
<li class="self-crumb">onElectronicHorizonUpdated abstract method</li>
</ol>
<h5>ElectronicHorizonListener class</h5>
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
