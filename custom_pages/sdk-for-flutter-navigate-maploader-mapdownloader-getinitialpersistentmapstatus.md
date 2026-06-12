---
title: "getInitialPersistentMapStatus abstract method"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-getinitialpersistentmapstatus"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getInitialPersistentMapStatus.html -->


<div>
<h1>getInitialPersistentMapStatus abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-maploader-persistentmapstatus">PersistentMapStatus</a>
getInitialPersistentMapStatus()

      

    

<p>Gets the initial status of the already downloaded regions at start-up time of the app.</p>
<p>It is not recommended to download or to upload map data while an app is running in
background. However, it can happen, that an app gets shut down during an ongoing
operation, for example, due to a crash. In such a case, some or all of the downloaded map data
may be in a corrupted state.
Refer to the <a href="/sdk-for-flutter-navigate-maploader-persistentmapstatus">PersistentMapStatus</a> for exact healing procedure for specific
status.
Note: This value will not change during the lifetime of an app.</p>
<p>Returns <a href="/sdk-for-flutter-navigate-maploader-persistentmapstatus">PersistentMapStatus</a>. Initial status of the persistent map.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">PersistentMapStatus getInitialPersistentMapStatus();</code></pre>

 



</div>
`
}</HTMLBlock>
