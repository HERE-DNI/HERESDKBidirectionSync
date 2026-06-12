---
title: "init static method"
slug: "sdk-for-flutter-navigate-core-sdkcontext-init"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- init.html -->


<div>
<h1>init static method</h1></div>

void
init([<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-isolateorigin">IsolateOrigin</a> isolateOrigin = IsolateOrigin.main</li>
</ol>])

      

    

<p>Prepares the SDK for use</p>
<p>Users should call this method once, when the application starts, preferably in the main()
method.</p>
<p><code>isolateOrigin</code> The isolate in which the application is executing.  This is IsolateOrigin.main
by default, and this is suitable for almost all use cases.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static void init([IsolateOrigin isolateOrigin = IsolateOrigin.main]) {
  LibraryContext.init(isolateOrigin, nativeLibraryPath: _getLibraryName());
  SDKDartInfo.version = Platform.version;
}</code></pre>

 



</div>
`
}</HTMLBlock>
