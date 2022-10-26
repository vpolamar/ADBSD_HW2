<html>
<body>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.btn {
  background-color: DodgerBlue;
  border: none;
  color: white;
  padding: 12px 16px;
  font-size: 16px;
  cursor: pointer;
}
</style>
<a href="/"><button class="btn"><i class="fa fa-home"></i>Home</button></a>
Edit this item...
<hr/>
<form action="/task1/edit/{{id}}" method="post">
  <p>Edit Item:<input name="description" value="{{description}}"/></p>
  <p><button type="submit">Submit</button></p>
</form>
<hr/>
<a href="/task1/list/">Cancel</a>
</body>
</html>