---
title: "destroyLockingProcess static method"
slug: "sdk-for-flutter-navigate-core-engine-lockingprocess-destroylockingprocess"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- destroyLockingProcess.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-navigate-core-engine-lockingprocess-class</li>
<li class="self-crumb">destroyLockingProcess static method</li>
</ol>
<div class="self-name">destroyLockingProcess</div>
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
<div class="main-content" data-above-sidebar="core.engine/LockingProcess-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>destroyLockingProcess static method</h1></div>
<section class="multi-line-signature">
void
destroyLockingProcess(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-engine-sdkoptions-class sdkOptions, </li>
<li>int maxTimeoutInMilliseconds</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Checks if cache folder is locked.</p>
<p>Does nothing if cache is not locked or locked by
current process. If cache is locked by a different process then the HERE SDK
makes a few attempts to kill the locking application during the specified timeout.
If it fails to kill the application, it attempts to remove the cache at
/sdk-for-flutter-navigate-core-engine-sdkoptions-cachepath. This function can be used before creating a SDKNativeEngine,
i.e.</p>
<pre class="language-dart"><code>final options = SDKOptions(...);
LockingProcess.destroyLockingProcess(options, 300);
final engine = SDKNativeEngine(options);
</code></pre>
<ul>
<li>
<p><code>sdkOptions</code> The options which are supposed to be used for a new instance of the engine.</p>
</li>
<li>
<p><code>maxTimeoutInMilliseconds</code> The maximum timeout in milliseconds. Recommended value is 300 - 500 milliseconds.
If 0 or a negative value is passed then it makes only one attempt to kill the locking
process (if any) and waits 30 milliseconds before exit because the system may spend a
small amount of time to perform the operation.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static void destroyLockingProcess(SDKOptions sdkOptions, int maxTimeoutInMilliseconds) =&gt; $prototype.destroyLockingProcess(sdkOptions, maxTimeoutInMilliseconds);</code></pre>
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
<li>/sdk-for-flutter-navigate-core-engine-lockingprocess-class</li>
<li class="self-crumb">destroyLockingProcess static method</li>
</ol>
<h5>LockingProcess class</h5>
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
