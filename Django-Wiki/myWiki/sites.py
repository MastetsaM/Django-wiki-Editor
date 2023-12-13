from wiki.sites import WikiSite
from myWiki.views import article

class MyWikiSite(WikiSite):
    def __init__(self, name="myWiki"):
        self.root_view = getattr(
            self,
            "root_view",
            article.CreateRootView.as_view()
        )
        
        self.article_edit_view = getattr(
            self, "article_edit_view", article.Edit.as_view()
        )

        self.article_create_view = getattr(
            self, "article_create_view", article.Create.as_view()
        )

        self = super().__init__(name)

