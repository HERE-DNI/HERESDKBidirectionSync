---
title: "destroyLockingProcess static method"
slug: "sdk-for-flutter-explore-core-engine-lockingprocess-destroylockingprocess"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- destroyLockingProcess.html -->


<div>
<h1>destroyLockingProcess static method</h1></div>

void
destroyLockingProcess(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-core-engine-sdkoptions-class">SDKOptions</a> sdkOptions, </li>
<li>int maxTimeoutInMilliseconds</li>
</ol>)

      

    

<p>Checks if cache folder is locked.</p>
<p>Does nothing if cache is not locked or locked by
current process. If cache is locked by a different process then the HERE SDK
makes a few attempts to kill the locking application during the specified timeout.
If it fails to kill the application, it attempts to remove the cache at
<a href="/sdk-for-flutter-explore-core-engine-sdkoptions-cachepath">SDKOptions.cachePath</a>. This function can be used before creating a SDKNativeEngine,
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


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static void destroyLockingProcess(SDKOptions sdkOptions, int maxTimeoutInMilliseconds) =&gt; $prototype.destroyLockingProcess(sdkOptions, maxTimeoutInMilliseconds);</code></pre>

 



</div>
`
}</HTMLBlock>
