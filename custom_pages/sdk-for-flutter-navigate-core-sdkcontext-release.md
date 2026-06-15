---
title: "release static method"
slug: "sdk-for-flutter-navigate-core-sdkcontext-release"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- release.html -->


<div>
<h1>release static method</h1></div>

void
release()

      

    

<p>Releases resources used by the SDK</p>
<p>Users should call this method once, when the application shuts down, preferably in the dispose()
method of the root widget's State.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static void release() {
  LibraryContext.release();
}</code></pre>

 



</div>
`
}</HTMLBlock>
