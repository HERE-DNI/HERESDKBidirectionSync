---
title: "taskCount property"
slug: "sdk-for-flutter-navigate-maploader-mapupdater-taskcount"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- taskCount.html -->


<div>
<h1>taskCount property</h1></div>
<section id="getter">

int
taskCount


<p>The number of concurrent tasks for downloading a map.
A valid task count is between 1 to 64. When the value set is outside the valid range,
then it is clamped to a valid range:</p>
<ul>
<li>when passed in value is 0 or less, then task count is set to 1;</li>
<li>when passed in value is 65 or more, then task count is set to 64.
Gets the number of concurrent tasks for downloading a map.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int get taskCount;</code></pre>

</section>
<section id="setter">

void
taskCount=(int value)


<p>The number of concurrent tasks for downloading a map.
A valid task count is between 1 to 64. When the value set is outside the valid range,
then it is clamped to a valid range:</p>
<ul>
<li>when passed in value is 0 or less, then task count is set to 1;</li>
<li>when passed in value is 65 or more, then task count is set to 64.
Sets the number of concurrent tasks for downloading a map.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set taskCount(int value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
