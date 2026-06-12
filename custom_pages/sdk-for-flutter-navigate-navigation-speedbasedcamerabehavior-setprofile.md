---
title: "setProfile abstract method"
slug: "sdk-for-flutter-navigate-navigation-speedbasedcamerabehavior-setprofile"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setProfile.html -->


<div>
<h1>setProfile abstract method</h1></div>

void
setProfile(<ol class="parameter-list single-line"> <li>List&lt;<a href="/sdk-for-flutter-navigate-navigation-speedbasedcamerabehaviorprofilevalue-class">SpeedBasedCameraBehaviorProfileValue</a>&gt; profile</li>
</ol>)

      

    

<p>Sets the profile.</p>
<p>The speed ranges within the profile can overlap in order to prevent oscillations between
adjacent levels.
Provided profile must satisfy following conditions:</p>
<ul>
<li>
<p>profile must not be empty</p>
</li>
<li>
<p>each speed range must be valid (fromMetersPerSecond must be less then toMetersPerSecond)</p>
</li>
<li>
<p>ranges must be sorted by fromMetersPerSecond and toMetersPerSecond</p>
</li>
<li>
<p>gaps between ranges are not allowed
Invalid profile will be rejected and error message logged with explanation of violated restriction.</p>
</li>
<li>
<p><code>profile</code> The new profile value.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setProfile(List&lt;SpeedBasedCameraBehaviorProfileValue&gt; profile);</code></pre>

 



</div>
`
}</HTMLBlock>
